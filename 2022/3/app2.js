const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
var sum = 0;
var elves = [];
var it = 0;
allFileContents.split(/\r?\n/).forEach(line =>  {
  if (line!=""){
    elves[it]= line.split('');
    if (it==2){
        const tmp = elves[0].filter(x => elves[1].indexOf(x)>=0).filter(x => elves[2].indexOf(x)>=0)[0].charCodeAt(0)-65;
        if (tmp>25){
            sum +=tmp-31;
        }else{
            sum+= tmp+27;
        }
        elves= [];
    }
    it = (it+1)%3;
  }
});
console.log(sum);
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
