const fs = require('fs');
var startDate = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

var lines = allFileContents.split(/\r?\n/);
lines = lines.map(x=>x.split('').map(y=>y.charCodeAt(0)))
xS = 0;
yS = 0;
xE = 0;
yE = 0;
start = false;
end = false;
while(!start || !end){
  if(lines[xS].indexOf('S'.charCodeAt(0))!=-1){
    yS = lines[xS].indexOf('S'.charCodeAt(0));
    lines[xS][yS]='a'.charCodeAt(0);
    start = true;
  }
  if(lines[xE].indexOf('E'.charCodeAt(0))!=-1){
    yE = lines[xE].indexOf('E'.charCodeAt(0));
    end = true;
    lines[xE][yE]='z'.charCodeAt(0);
  }
  if (!start){
    xS++;
  }
  if (!end){
    xE++;
  }
}
print = function(arr){
    for (const line of arr){
        console.log(line.map(x=>x==7224?'.':x).join(''))
    }
}
step = function(i,j){
  if (i-1>=0 && ((lines[i-1][j]-lines[i][j])<=1) && distance[i-1][j]>(distance[i][j]+1)){
    distance[i-1][j]=distance[i][j]+1;
    step(i-1,j);
  }
  if (j-1>=0 && ((lines[i][j-1]-lines[i][j])<=1) && distance[i][j-1]>(distance[i][j]+1)){
    distance[i][j-1]=distance[i][j]+1;
    step(i,j-1);
  }
if (i+1<lines.length && ((lines[i+1][j]-lines[i][j])<=1) && distance[i+1][j]>(distance[i][j]+1)){
    distance[i+1][j]=distance[i][j]+1;
    step(i+1,j);
  }
if (j+1<lines[i].length && ((lines[i][j+1]-lines[i][j])<=1) && distance[i][j+1]>(distance[i][j]+1)){
    distance[i][j+1]=distance[i][j]+1;
    step(i,j+1);
  }

}
console.log("ending at "+xE+" "+yE)

var min=lines.length*lines[0].length;
for (let xS=0;xS<lines.length;xS++){
    for (let yS=0;yS<lines[xS].length;yS++){
        if (lines[xS][yS]=='a'.charCodeAt(0)){
            var distance = lines.map((x,i)=>x.map((y,j)=>(j==yS)&&(i==xS)?0:lines.length*x.length ));
            step(xS,yS);
            const dis = distance[xE][yE];
            min = min>dis?dis:min;
        }
    }
}

console.log(min)


const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - startDate
console.info('Execution time: %dms', end)