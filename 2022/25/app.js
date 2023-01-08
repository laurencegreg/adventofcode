const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

const dictValue = { '2': 2, '1': 1, '0': 0, '-':-1,'=':-2 }

const dictRevert = { 2: '2', 1: '1', 0: '0'};
dictRevert[-1]='-';
dictRevert[-2]='=';

const lines = allFileContents.split(/\r?\n/);
sum = 0;
lines.forEach(line=>{
    const len = line.length-1;
    line.split('').map(x=>dictValue[x]).forEach((x,i)=>sum+=Math.pow(5,(len-i))*x);
})

var res = "";
var step = sum; 
while(step!=0){
    var next = Math.floor(step/5);
    var car = step - next*5;
    if (car>2){
        car = car-5;
        next = next+1;
    }
    res = dictRevert[car]+res;
    step = next;
}

console.log("part 1 : "+res);
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start;
console.info('Execution time: %dms', end);