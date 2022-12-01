const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
var elves = [];
var tmpElf = 0;
allFileContents.split(/\r?\n/).forEach(line =>  {
  if (line==""){
    elves.push(tmpElf);
    tmpElf = 0;
  }else{
    tmpElf += Number(line);
  }
});
elves.sort(function (a, b) {  return a - b;}).reverse();
console.log("step 1 : "+elves[0]);
console.log("step 2 : "+(elves[0]+elves[1]+elves[2]));
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
