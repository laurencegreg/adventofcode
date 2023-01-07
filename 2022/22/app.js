const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

const dirs = ["right","down","left","up"]

function Pos(x, y,full) {
    this.x = x;
    this.y = y;
    this.full = full;
    this.neighbors = [];
   
}

const lines = allFileContents.split(/\r?\n/);
const high = lines.length-2;
var weight = 0;
const posArray = [];
lines.forEach((line,x) => {
    if (line.length>weight){
        weight = line.length;
    }
    if (x < high) {
        posArray.push(line.split('').map((c,y)=>{
            if (c=="."){
                return new Pos(x,y,false);
            }else if (c=="#"){
                return new Pos(x,y,true);
            }
        }))
    }
})
for(let x=0;x<high;x++){
    for(let y=0;y<weight;y++){
        const pos = posArray[x][y];
        if (pos != undefined){
            //left
            var move = ((y-1)+weight)%weight;
            while(posArray[x][move]==undefined){
                move = ((move-1)+weight)%weight;
            }
            pos.neighbors[2] = posArray[x][move];
            //right
            var move = (y+1)%weight;
            while(posArray[x][move]==undefined){
                move = (move+1)%weight;
            }
            pos.neighbors[0] = posArray[x][move];
            //up
            var move = ((x-1)+high)%high;
            while(posArray[move][y]==undefined){
                move = ((move-1)+high)%high;
            }
            pos.neighbors[3] = posArray[move][y];
            //down
            var move = (x+1)%high;
            while(posArray[move][y]==undefined){
                move = (move+1)%high;
            }
            pos.neighbors[1] = posArray[move][y];

        }
    }
}
var leftMost = 0;
while(posArray[0][leftMost]==undefined){
    leftMost++;
}

var path = lines[lines.length-1].split(/(L|R)/g).map(x=>((x=='L')||(x=='R'))?x:Number(x));
var direction = 0;
var position = posArray[0][leftMost];
while((path.length!=1)||(path[0]!=0)){
    if (path[0]==0){
        console.log("reach "+(position.x+1)+" "+(position.y+1))
        const turn = path[1];
        var dir = direction;
        if (turn=="R"){
            dir = (dir+1)%4;
        }else{
            dir = (dir+3)%4;
        }
        console.log("go "+dirs[dir]);
        direction = dir;
        path = path.slice(2);
    }else{
        if (position.neighbors[direction].full){
            path[0]=0;
        }else{
            path[0]=path[0]-1;
            position=position.neighbors[direction];
        }
    }
}

console.log("end position : "+(position.x+1)+" "+(position.y+1)+" direction "+dirs[direction]+"("+direction+")")
console.log("part 1 : "+((position.x+1)*1000+(position.y+1)*4+direction));

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start;
console.info('Execution time: %dms', end);