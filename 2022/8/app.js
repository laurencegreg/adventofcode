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
var visibles = 0;
for (let i = 0; i < forest.length; i++) {
    for (let j = 0; j < forest[i].length; j++) {
        var visible = (i==0)||(j==0)||(i==forest.length-1)||(j==forest[i].length-1);
        var hidden = false;
        var tmpj = j;
        while (!visible && !hidden && (tmpj>0)){
            tmpj -=1;
            if (forest[i][j]<=forest[i][tmpj]){
                hidden = true;
            }
            if (tmpj==0){
                visible = visible || !hidden;
            }
        }

        tmpj = j;
        hidden = false;
        while (!visible && !hidden && (tmpj<(forest[i].length-1))){
            tmpj +=1;
            if (forest[i][j]<=forest[i][tmpj]){
                hidden = true;
            }
            if (tmpj==(forest[i].length-1)){
                visible = visible || !hidden;
            }
        }

        var tmpi = i;
        hidden = false;
        while (!visible && !hidden && (tmpi>0)){
            tmpi -=1;
            if (forest[i][j]<=forest[tmpi][j]){
                hidden = true;
            }
            if (tmpi==0){
                visible = visible || !hidden;
            }
        }

        tmpi = i;
        hidden = false;
        while (!visible && !hidden && (tmpi<(forest.length-1))){
            tmpi +=1;
            if (forest[i][j]<=forest[tmpi][j]){
                hidden = true;
            }
            if (tmpi==(forest.length-1)){
                visible = visible || !hidden;
            }
        }
        if (visible){
            visibles +=1;
        }
    }
}

console.log(`part 1 : ${visibles} trees visibles`)

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
