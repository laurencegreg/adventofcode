const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

var bluePrints = [];
const resourceDict = {'ore':0,'clay':1,'obsidian':2,'geode':3};

function BluePrint() {

    this.cost = [] ;
    this.maxCost = [];
    this.doTheMax = function(){
        for (let i=0;i<this.cost[0].length;i++){
            this.maxCost.push(Math.max(...this.cost.map(x=>x[i])));
        }
        this.maxCost[this.maxCost.length-1]=999;
    }
    this.canConstruct = function(resources){
        return this.cost.map(c =>c.map((x,i)=>resources[i]>=x).reduce((tmp, a) => tmp && a, true))
    }

    this.produce = function(resources,diggers){
        return resources.map((x,i)=>x+diggers[i]);
    }

    this.step = function(resources,diggers,nb){
        const nextResources = this.produce(resources,diggers);
        if (nb==1){
            return nextResources[resourceDict['geode']];
        }
        const weCan = this.canConstruct(resources);
        if (weCan[3]){
            const nextDiggers = [...diggers];
            nextDiggers[3]+=1;
            return this.step(nextResources.map((y,j)=>y-this.cost[3][j]),nextDiggers,nb-1);
        }
        var res = this.step(nextResources,diggers,nb-1);
        weCan.forEach((x,i)=>{
            if (x && (diggers[i]<this.maxCost[i])){
                const nextDiggers = [...diggers];
                nextDiggers[i]+=1;
                const tmp = this.step(nextResources.map((y,j)=>y-this.cost[i][j]),nextDiggers,nb-1);
                if (tmp>res){
                    res = tmp;
                }
            }
        })
        return res;
    }
}

allFileContents.split(/\r?\n/).forEach(line => {
    if (line != "") {
        const b = new BluePrint();
        line.split('.').forEach(subline =>{

    if (subline != "") {
        const lineRe = new RegExp('Each ([a-z]+) robot costs (.*)', 'g');
        const extract = lineRe.exec(subline);
        const arr = [0,0,0,0];
        extract[2].split(' and ').forEach(x=>{
            const sp = x.split(' ');
            arr[resourceDict[sp[1]]]=Number(sp[0]);
        })
        b.cost[resourceDict[extract[1]]] = arr;
    }
    
    })
    b.doTheMax();
    bluePrints.push(b);
    }

})
const STEP = 24;
var final = 0;
for(let ind=0;ind<bluePrints.length;ind++){
    console.log(bluePrints[ind]);
    const res = bluePrints[ind].step([0,0,0,0],[1,0,0,0],STEP);
    console.log(`${res} geodes for ${ind+1}`);
    final += (res*(ind+1));
}
console.log("part 1 : "+final);
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start;
console.info('Execution time: %dms', end);
