const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

var monkeys = []
function Monkey(id) {

    this.id = id;
    this.ops = [];
    this.test = null;
    this.operation = null;
    this.ok = -1;
    this.ko = -1;
    this.inspect = 0;
    
    this.addOp = function(op){
        this.ops.push(op)
    }

    this.setTest = function(test) {
        this.test = test;
    }

    this.setOperation = function(operation) {
        this.operation = function(op){return Math.floor(operation(op)/3)};
    }

    this.setOk = function(id){
        this.ok = id;
    }

    this.setKo = function(id){
        this.ko = id;
    }

    this.hasStep = function(){
        return this.ops.length != 0;
    }
    
    this.step = function(){
        this.inspect++;
        const op = this.operation(this.ops.shift());
        var monk = monkeys[this.ko]
        if(this.test(op)){
            monk = monkeys[this.ok]
        }
        monk.addOp(op);
    }
}

const lines = allFileContents.split(/\r?\n/);
var ind = 0;
while (ind+5 < lines.length){
    const monk = new Monkey(Number(lines[ind].split(' ')[1].split(':')[0]));
    lines[ind+1].split(':')[1].trim().split(",").map(x => monk.addOp(Number(x)));
    var line = lines[ind+2].split(" ");
    switch(line[line.length-2]){
        case '+':
            if (line[line.length-1]!="old"){
                const y = Number(line[line.length-1]);
                monk.setOperation(function(x){return x+y});
            }else {
                monk.setOperation(function(x){return x+x});
            }
            break;
        case '*':
            if (line[line.length-1]!="old"){
                const y = Number(line[line.length-1]);
                monk.setOperation(function(x){return x*y});
            }else {
                monk.setOperation(function(x){return x*x});
            }
            break;
    }
    line = lines[ind+3].split(" ");
    const y = Number(line[line.length-1]);
    monk.setTest(function(x){return (x % y)==0});
    line = lines[ind+4].split(" ");
    monk.setOk(Number(line[line.length-1]));
    line = lines[ind+5].split(" ");
    monk.setKo(Number(line[line.length-1]));
    monkeys.push(monk);
    ind+=7;
}
for(let i=0;i<20;i++){
    for (const monkey of monkeys) {
        while (monkey.hasStep()){
            monkey.step();
        }
    }
}
for (const monkey of monkeys) {
    console.log(`Monkey ${monkey.id} inspected items ${monkey.inspect} times.`);
}
const inspections = monkeys.map(x=>x.inspect).sort(function (a, b) {  return a - b;  }).reverse();
console.log("part 1 : "+(inspections[0]*inspections[1]));
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
