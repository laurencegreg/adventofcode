const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
var stacks =[[],[],[],[],[],[],[],[],[]]
const lines = allFileContents.split(/\r?\n/)
var line = lines[0];
var index = 1;
  while (!line.includes('1')){
      var it = 0;
      while ((it*4+1)<line.length){
        if (line[it*4+1]!=' '){
            stacks[it].push(line[it*4+1]);
        }
        it++;
      }
      line=lines[index];
      index++;
  }
index++;
stacks = stacks.map(x=>x.reverse());
while(index< lines.length &&lines[index]!=''){
    const splitted = lines[index].split(' ')
    const nb = Number(splitted[1]);
    const from = Number(splitted[3]);
    const to = Number(splitted[5]);
    const crates = stacks[from-1].slice(stacks[from-1].length-nb);
    stacks[from-1]= stacks[from-1].slice(0,(stacks[from-1].length-nb));
    stacks[to-1]=stacks[to-1].concat(crates);
    index++
}

console.log(stacks.map(x=> x[x.length-1]).join(''))
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
