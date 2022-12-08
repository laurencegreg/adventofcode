const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

var forest = [] 
allFileContents.split(/\r?\n/).forEach(line =>  {
  if ((line!="")){
    forest.push(line.split('').map(x => Number(x)));
  }
});


//part 1
var maxScenic = 0;
for (let i = 0; i < forest.length; i++) {
    for (let j = 0; j < forest[i].length; j++) {
        var hidden = false;
        var tmpj = j;
        var a = 0;
        var b = 0;
        var c = 0;
        var d = 0;
        while (!hidden && (tmpj>0)){
            tmpj -=1;
            a++;
            if (forest[i][j]<=forest[i][tmpj]){
                hidden = true;
            }
        }

        tmpj = j;
        hidden = false;
        while (!hidden && (tmpj<(forest[i].length-1))){
            tmpj +=1;
            b++;
            if (forest[i][j]<=forest[i][tmpj]){
                hidden = true;
            }
        }

        var tmpi = i;
        hidden = false;
        while (!hidden && (tmpi>0)){
            tmpi -=1;
            c++;
            if (forest[i][j]<=forest[tmpi][j]){
                hidden = true;
            }
            
        }

        tmpi = i;
        hidden = false;
        while (!hidden && (tmpi<(forest.length-1))){
            tmpi +=1;
            d++;
            if (forest[i][j]<=forest[tmpi][j]){
                hidden = true;
            }
        }

        const scenic = a*b*c*d;
        maxScenic = maxScenic<scenic?scenic:maxScenic;
        
    }
}

console.log(`part 2 : ${maxScenic} max scenic`)

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
