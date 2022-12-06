const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
const line = allFileContents.split(/\r?\n/)[0];

function findStart(length){
    var index = length;
    while(line.substring(index-length,index).split('').sort().reduce((accumulator, currentValue,i,array1) => i==0?false:(accumulator || array1[i-1]==currentValue),false)){
        index++
    };
    return index;
}
console.log("step 1 : "+findStart(4));
console.log("step 2 : "+findStart(14));
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
