const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

var res = 0;

allFileContents.split(/\r?\n/).forEach(line =>  {
  if (line!=""){
   res+=Number(line); 
  }
});

console.log(res);
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
