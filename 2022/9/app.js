const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
var hx = 0;
var hy = 0;
var tx = 0;
var ty = 0;

var mx = {"R":1,"L":-1,"U":0,"D":0}
var my = {"R":0,"L":0,"U":1,"D":-1}
const pos = new Set()
pos.add("0:0")
allFileContents.split(/\r?\n/).forEach(line =>  {
  if ((line!="")){
    const splitted = line.split(" ");
    for(let i=0;i<Number(splitted[1]);i++){
        hx += mx[splitted[0]];
        hy += my[splitted[0]];
        if ((Math.abs(hx-tx)>1) || (Math.abs(hy-ty)>1)){
            if (Math.abs(hx-tx)==2){
                if (Math.abs(hy-ty)==1){
                    ty +=(hy-ty)
                }
                tx += ((hx-tx)/2);
            }else{
                if (Math.abs(hx-tx)==1){
                    tx +=(hx-tx)
                }
                ty += ((hy-ty)/2);
            }
            pos.add(`${tx}:${ty}`)

        }
    }
  }
});

console.log(pos.size)

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
