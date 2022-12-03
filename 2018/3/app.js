const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
var counts = {}
allFileContents.split(/\r?\n/).forEach(line =>  {
    if (line!=""){
        //#2 @ 3,1: 4x4
        const data = line.split(' ');
        const id = data[0].replace('#','')
        const x = Number(data[2].split(',')[0])
        const y = Number(data[2].split(',')[1].replace(':',''))
        const i = Number(data[3].split('x')[0])
        const j = Number(data[3].split('x')[1])
        for (let a=x;a<x+i;a++){
            for (let b=y;b<y+j;b++){
                const id = a+":"+b
                counts[id] = (counts[id] || 0) + 1;
            }
        }
    };
});
console.log(Object.values(counts).map(x => (x==1)?0:1).reduce((a,c) => a+c,0))

//step 2
allFileContents.split(/\r?\n/).forEach(line =>  {
    if (line!=""){
        //#2 @ 3,1: 4x4
        const data = line.split(' ');
        const id = data[0].replace('#','')
        const x = Number(data[2].split(',')[0])
        const y = Number(data[2].split(',')[1].replace(':',''))
        const i = Number(data[3].split('x')[0])
        const j = Number(data[3].split('x')[1])
        var ok = true
        for (let a=x;a<x+i;a++){
            for (let b=y;b<y+j;b++){
                const id = a+":"+b
                ok = ok && (counts[id]==1);
            }
        }
        if (ok){
            console.log(id)
        }
    };
});
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
