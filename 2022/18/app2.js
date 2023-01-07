const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

cubePos = new Set();
cubes = [];
var xMax = 0;
var xMin = 100;
var yMax = 0;
var yMin = 100;
var zMax = 0;
var zMin = 100;

function Cube(coord) {

    this.x = coord[0];
    if (xMax < this.x) {
        xMax = this.x;
    }
    if (xMin > this.x) {
        xMin = this.x;
    }
    this.y = coord[1];
    if (yMax < this.y) {
        yMax = this.y;
    }
    if (yMin > this.y) {
        yMin = this.y;
    }
    this.z = coord[2];
    if (zMax < this.z) {
        zMax = this.z;
    }
    if (zMin > this.z) {
        zMin = this.z;
    }

    this.emptySides = function () {
        return 0
            + (!cubePos.has((this.x - 1) + "," + this.y + "," + this.z))
            + (!cubePos.has((this.x + 1) + "," + this.y + "," + this.z))
            + (!cubePos.has(this.x + "," + (this.y - 1) + "," + this.z))
            + (!cubePos.has(this.x + "," + (this.y + 1) + "," + this.z))
            + (!cubePos.has(this.x + "," + this.y + "," + (this.z - 1)))
            + (!cubePos.has(this.x + "," + this.y + "," + (this.z + 1)));
    }
}

allFileContents.split(/\r?\n/).forEach(line => {
    if (line != "") {
        cubePos.add(line);
        cubes.push(new Cube(line.split(",").map(x => Number(x))));
    }
})

console.log(cubes.map(x => x.emptySides()).reduce((tmp, a) => tmp + a, 0));

for (x = xMin; x <= xMax; x++) {
    for (y = yMin; y <= yMax; y++) {
        for (z = zMin; z <= zMax; z++) {
            if (!cubePos.has(x + "," + y + "," + z)) {
                const regexX = new RegExp("^([1-9]+)," + y + "," + z+"$");
                const resX = [...cubePos].map(s => s.match(regexX)).filter(s => s != null).map(s => Number(s[1]));
                if ((Math.min(...resX) < x) && (Math.max(...resX) > x)) {
                    const regexY = new RegExp("^"+x + ",([1-9]+)," + z+"$");
                    const resY = [...cubePos].map(s => s.match(regexY)).filter(s => s != null).map(s => Number(s[1]));
                    if ((Math.min(...resY) < y) && (Math.max(...resY) > y)) {
                        const regexZ = new RegExp("^"+x +","+y+",([1-9]+)$");
                        const resZ = [...cubePos].map(s => s.match(regexZ)).filter(s => s != null).map(s => Number(s[1]));
                        if ((Math.min(...resZ) < z) && (Math.max(...resZ) > z)) {
                            cubePos.add(x+","+y+","+z);
                            cubes.push(new Cube([x,y,z]));
                        }
                    }
                }
            }
        }
    }
}

console.log(cubes.map(x=>x.emptySides()).reduce((tmp, a) => tmp + a, 0));

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start;
console.info('Execution time: %dms', end);