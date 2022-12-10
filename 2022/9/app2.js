const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

var mx = {"R":1,"L":-1,"U":0,"D":0}
var my = {"R":0,"L":0,"U":1,"D":-1}
const pos10 = new Set()
const pos2 = new Set()
const rope = Array.from({length: 10}, () => [0,0])
pos10.add("0:0")
pos2.add("0:0")
allFileContents.split(/\r?\n/).forEach(line =>  {
  if ((line!="")){
    const splitted = line.split(" ");
    for(let a=0;a<Number(splitted[1]);a++){
        rope[0][0] += mx[splitted[0]];
        rope[0][1] += my[splitted[0]];
        var i = 1;
        while((i<rope.length)&&((Math.abs(rope[i-1][0]-rope[i][0])>1) || (Math.abs(rope[i-1][1]-rope[i][1])>1))){
            if (Math.abs(rope[i-1][0]-rope[i][0])==2){
                if (Math.abs(rope[i-1][1]-rope[i][1])==2){
                    rope[i][1] +=((rope[i-1][1]-rope[i][1])/2);
                }else if (Math.abs(rope[i-1][1]-rope[i][1])==1){
                    rope[i][1] +=(rope[i-1][1]-rope[i][1])
                }
                rope[i][0] += ((rope[i-1][0]-rope[i][0])/2);
            }else{
                if (Math.abs(rope[i-1][0]-rope[i][0])==1){
                    rope[i][0] +=(rope[i-1][0]-rope[i][0])
                }
                rope[i][1] += ((rope[i-1][1]-rope[i][1])/2);
            }
            i++;

        }
        pos10.add(`${rope[9][0]}:${rope[9][1]}`);
        pos2.add(`${rope[1][0]}:${rope[1][1]}`)
    }
  }
});

console.log(`part 1 : ${pos2.size}`)
console.log(`part 2 : ${pos10.size}`)

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
