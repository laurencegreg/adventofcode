const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
var coords = allFileContents.split(/\r?\n/).map(x => [Number(x), false]);
coords.pop();
var ind = 0;
print = function (arr) {
    console.log(arr.map(x => x[0]))
}
for (let i = 0; i < coords.length; i++) {
    while (coords[ind][1]) {
        ind++;
    }
    const mv = coords[ind][0];
    coords=coords.filter((_, i) => i != ind);
    var dest = (mv + ind)%coords.length;
    if (dest==0){
        coords = [...coords,[mv,true]];
    }else{
        coords.splice(dest,0,[mv,true]);
    }
}
const res = coords.map(x => x[0]);
const zero = res.indexOf(0);
console.log(res[(zero + 1000) % res.length] + res[(zero + 2000) % res.length] + res[(zero + 3000) % res.length])

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start;
console.info('Execution time: %dms', end);