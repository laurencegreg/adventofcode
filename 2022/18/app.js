const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

cubePos = new Set();
cubes = [];
function Cube(coord){
    this.x = coord[0];
    this.y = coord[1];
    this.z = coord[2];

    this.emptySides = function(){
        return 0
            + (!cubePos.has((this.x-1)+","+this.y+","+this.z))
            + (!cubePos.has((this.x+1)+","+this.y+","+this.z))
            + (!cubePos.has(this.x+","+(this.y-1)+","+this.z))
            + (!cubePos.has(this.x+","+(this.y+1)+","+this.z))
            + (!cubePos.has(this.x+","+this.y+","+(this.z-1)))
            + (!cubePos.has(this.x+","+this.y+","+(this.z+1)));
    }
}

allFileContents.split(/\r?\n/).forEach(line => {
    if (line != "") {
        cubePos.add(line);
        cubes.push(new Cube(line.split(",").map(x=>Number(x))));
    }
})

console.log(cubes.map(x=>x.emptySides()).reduce((tmp, a) => tmp + a, 0));

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start;
console.info('Execution time: %dms', end);