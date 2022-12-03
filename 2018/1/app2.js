const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

var frequences = [];
var last = 0;
var index = 0;
const lines = allFileContents.split(/\r?\n/);
const nbLines = lines.length-1;
while (frequences.indexOf(last)==-1){
    frequences.push(last);
    last +=Number(lines[index%nbLines]);
    index +=1;
}

console.log(last);
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
