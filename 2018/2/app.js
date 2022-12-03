const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
var elves = [];
var tmpElf = 0;

var countTwo = 0;
var countThree = 0;
allFileContents.split(/\r?\n/).forEach(line =>  {
  if (line!=""){
    const chars = [...line].sort();
    var two = false;
    var three = false;
    var tmpTwo = false;
    var tmpThree = false;
    var last = "";
    chars.forEach(char => {
      if (last == char){
        if (tmpThree){
          tmpThree=false;
        }else if(tmpTwo){
          tmpTwo=false;
          tmpThree=true;
        }else{
          tmpTwo=true;
        }
      }else{
        two = tmpTwo || two;
        three = three || tmpThree; 
        tmpThree=false;
        tmpTwo=false;
      }
      last = char
    })
    two = tmpTwo || two;
    three = three || tmpThree; 
    if (three){
        countThree ++;
    }
    if (two){
        countTwo ++;
    }
  }
});

console.log(countTwo+"*"+countThree+"="+(countTwo*countThree));
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
