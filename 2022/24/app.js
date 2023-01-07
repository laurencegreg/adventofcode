const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

const dictMove = { '>': [0, 1], '^': [-1, 0], '<': [0, -1], 'v': [1, 0] }
const lines = allFileContents.split(/\r?\n/);

var blizzard = lines.map(x => x.split('')).map(x => x.map(y => y != '.' ? [y] : []));

init = function(height,width){
    //init array
    var arr = new Array();
    for (let i = 0; i < height; i++) {
        var tmpArr = new Array();
        for (let j = 0; j < width; j++) {
            tmpArr.push([]);
        }
        arr.push(tmpArr);
    }
    return arr;
}
blizzardStep = function (prevArr) {
    const nextArr = init(prevArr.length,prevArr[0].length);
    //move blizzard
    for (let i = 0; i < prevArr.length; i++) {
        for (let j = 0; j < prevArr[i].length; j++) {
            var tmpArr = prevArr[i][j];
            if (tmpArr.includes('#')) {
                nextArr[i][j].push('#');
            } else {
                tmpArr.forEach(m => {
                    const dir = dictMove[m];
                    var tmpI = i + dir[0];
                    var tmpJ = j + dir[1];
                    if (tmpI == 0) {
                        tmpI = prevArr.length - 2;
                    } else if (tmpI == prevArr.length - 1) {
                        tmpI = 1;
                    }
                    if (tmpJ == 0) {
                        tmpJ = prevArr[i].length - 2;
                    } else if (tmpJ == prevArr[i].length - 1) {
                        tmpJ = 1;
                    }
                    nextArr[tmpI][tmpJ].push(m);
                })
            }
        }
    }
    return nextArr;
}

print = function(arr){
    arr.forEach(line=>{
        console.log(line.map(x=>{
            if (x.length==0){
                return '.'
            }else if (x.length>1){
                return x.length
            }else{
                return x[0]
            }
        }).join(''))
    })
}

move = function(pos,blizzard){
    var nextPos = init(pos.length,pos[0].length);
    for (let i = 0; i < pos.length; i++) {
        for (let j = 0; j < pos[i].length; j++) {
            if(pos[i][j]=='E'){
               
                if ((i>0)&&(blizzard[i-1][j].length==0)){
                    nextPos[i-1][j]='E';
                }
                if (blizzard[i][j].length==0){
                    nextPos[i][j]='E';
                }
                if (((i+1)<pos.length)&&(blizzard[i+1][j].length==0)){
                    nextPos[i+1][j]='E';
                }
                if ((j>0)&&(blizzard[i][j-1].length==0)){
                    nextPos[i][j-1]='E';
                }
                if (((j+1)<pos[i].length)&&(blizzard[i][j+1].length==0)){
                    nextPos[i][j+1]='E';
                }
            }
        }
    }
    return nextPos
}

var pos = init(blizzard.length,blizzard[0].length)
var step = 0;
pos[0][1]='E'
//print(blizzard);
//print(pos);
while(pos[pos.length-1][pos[0].length-2]!='E'){
    step +=1;
    //console.log("//// step "+step+" ////");
    blizzard = blizzardStep(blizzard);
    //print(blizzard);
    pos = move(pos,blizzard);
    //print(pos);
}

console.log("part 1 : "+step)
var pos = init(blizzard.length,blizzard[0].length)
pos[pos.length-1][pos[0].length-2]='E';

while(pos[0][1]!='E'){
    step +=1;
    //console.log("//// step "+step+" ////");
    blizzard = blizzardStep(blizzard);
    //print(blizzard);
    pos = move(pos,blizzard);
    //print(pos);
}

console.log("back : "+step)
var pos = init(blizzard.length,blizzard[0].length)
pos[0][1]='E'

while(pos[pos.length-1][pos[0].length-2]!='E'){
    step +=1;
    //console.log("//// step "+step+" ////");
    blizzard = blizzardStep(blizzard);
    //print(blizzard);
    pos = move(pos,blizzard);
    //print(pos);
}

console.log("part 2 : "+step)

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start;
console.info('Execution time: %dms', end);