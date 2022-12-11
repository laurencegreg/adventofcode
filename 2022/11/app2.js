const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

var monkeys = [];
var opsModulo = [];

function Monkey(id) {

    this.id = id;
    this.ops = [];
    this.operation = null;
    this.ok = -1;
    this.ko = -1;
    this.inspect = 0;
    this.modulo = 0;
    
    this.addOp = function(op){
        this.ops.push(op);
    }

    this.test = function(idOp) {
        return opsModulo[idOp][this.id]==0;
    }

    this.setModulo = function(modulo) {
        this.modulo = modulo;
    }

    this.setOperation = function(operation) {
        this.operation = operation;
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
        const op = this.ops.shift();
        opsModulo[op] = opsModulo[op].map((x,n)=>this.operation(x)%monkeys[n].modulo);
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
    for (const opLine of lines[ind+1].split(':')[1].trim().split(",")){
        monk.addOp(opsModulo.length);
        opsModulo.push(Number(opLine));
    }
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
    monk.setModulo(y);
    line = lines[ind+4].split(" ");
    monk.setOk(Number(line[line.length-1]));
    line = lines[ind+5].split(" ");
    monk.setKo(Number(line[line.length-1]));
    monkeys.push(monk);
    ind+=7;
}

opsModulo = opsModulo.map(x=>(monkeys.map(y=>x%(y.modulo))));


for(let i=0;i<10000;i++){
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
console.log("part 2 : "+(inspections[0]*inspections[1]));
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
