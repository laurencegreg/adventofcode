const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

function diff(s,s2){
    var nbDiff = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i]!=s2[i]){
            nbDiff ++;
        }   
    }
    return nbDiff;
}

console.log(diff("abcde","abxde"))
const lines = allFileContents.split(/\r?\n/)
var i = -1;
found = false;
while (!found){
    i++;
    var j= i;
    while (!found && j<lines.length-2){
        j++;
        found=(diff(lines[i],lines[j])==1);
    }
}

console.log(lines[i]+" -> "+lines[j]);
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
