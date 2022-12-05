const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
var over = 0;
var miniOver = 0;
allFileContents.split(/\r?\n/).forEach(line =>  {
  if (line!=""){
    const elves = line.split(',');
    const elf1 = elves[0].split('-');
    const elf2 = elves[1].split('-');
    const x1=Number(elf1[0]);
    const y1=Number(elf1[1]);
    const x2=Number(elf2[0]);
    const y2=Number(elf2[1]);
    if (((x1>=x2)&&(y1<=y2))||((x2>=x1)&&(y2<=y1))){
        over++;
    }
    if ((((x1>=x2)&&(x1<=y2))||((y1>=x2)&&(y1<=y2)))||(((x2>=x1)&&(x2<=y1))||((y2>=x1)&&(y2<=y1)))){
        miniOver++;
    }
  }
});
console.log("overlaps : "+over);
console.log("overlaps a little: "+miniOver);
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
