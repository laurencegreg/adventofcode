const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
var x = 1;
var cycle = 0;
var sum = 0;
const crt = Array.from({length: 6}, () => Array(40).fill('.'));
allFileContents.split(/\r?\n/).forEach(line =>  {
  if ((line!="")){
    const splitted = line.split(' ');
    if (cycle%40==19){
        console.log(`start of cycle ${cycle+1} : x = ${x} and sum = ${sum}`)
        sum += (x*(cycle+1));
        console.log(`end of cycle ${cycle+1} : sum = ${sum}`)
    }
    if (x-1<=(cycle%40) && x+1>=(cycle%40)){
        crt[Math.floor(cycle/40)][cycle%40]='#';
    }
    if (splitted[0]=="noop"){
        cycle+=1;
    }else{
        cycle+=1;
        if (cycle%40==19){
            console.log(`start of cycle ${cycle+1} : x = ${x} and sum = ${sum}`)
            sum += (x*(cycle+1));
            console.log(`end of cycle ${cycle+1} : sum = ${sum}`)
        }
        if (x-1<=(cycle%40) && x+1>=(cycle%40)){
            crt[Math.floor(cycle/40)][cycle%40]='#';
        }
        x+=Number(splitted[1]);
        cycle+=1;
    }
  }
});

console.log(`part 1 : ${sum}`);
console.log(`part 2 :`);
console.log(crt.map(x=>x.join('')));
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
