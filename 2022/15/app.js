const fs = require('fs');
const util = require('util')
var startDate = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
var emptyPos = new Array();
var occupedPos = new Set();
const checkedLine = 2000000;
allFileContents.split(/\r?\n/).forEach(line => {
    if (line != "") {
        const lineRe = new RegExp('Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)', 'g');
        const extract = lineRe.exec(line);
        const xS = Number(extract[1]);
        const yS = Number(extract[2]);
        const xB = Number(extract[3]);
        const yB = Number(extract[4]);
        if (yS == checkedLine){
            occupedPos.add(xS+","+yS);
        }
        if (yB == checkedLine){
            occupedPos.add(xB+","+yB);
        }
        const distX = Math.abs(xS - xB);
        const distY = Math.abs(yS - yB);
        const dist = distX + distY;
        if ((checkedLine>=yS-dist)&&(checkedLine<=yS+dist)){
            const xMax = dist-Math.abs(yS-checkedLine);
            emptyPos.push([(xS-xMax),(xS+xMax)]);
        }
        // for (let x = xS - dist; x <= xS + dist; x++) {
        //     const yMax = dist - Math.abs(x - xS);
        //     for (let y = yS - yMax; y <= yS + yMax; y++) {
        //         emptyPos.add(x + "," + y);
        //     }
        // }
    }
})

const occPoints = [...occupedPos].map(x=>x.split(",").map(y=>Number(y)));
const emptySp = emptyPos.sort(function (a, b) {  return a[0] - b[0];  });
const emptyBand = [];
var left = emptySp[0][0];
var right = emptySp[0][1];
var ind = 1;
while(ind<emptySp.length){
    if (emptySp[ind][1]>right){
        if (emptySp[ind][0]<=right){
            right = emptySp[ind][1];
        }else{
            emptyBand.push([left,right]);
            left=emptySp[ind][0];
            right=emptySp[ind][1];
        }
    }
    ind++;
}
emptyBand.push([left,right]);
console.log("part 1 : "+(emptyBand[0][1]-emptyBand[0][0]));
//console.log([...emptyPos].filter(x=>(!occupedPos.has(x))).filter(x=> x.includes(",2000000")).length);

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - startDate
console.info('Execution time: %dms', end)