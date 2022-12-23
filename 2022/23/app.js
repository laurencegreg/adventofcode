const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input.test', 'utf-8');

var elves = [];
var elvesPos = [];
var testDir = [];
var setDir = [];
var index = 0;
//north
testNorth = function (x, y) {
    var north = false;
    for (let j = (y - 1); j <= (y + 1); j++) {
        north = north || elvesPos.includes((x - 1) + "," + j);
    }
    return north;
}
setNorth = function (x, y) {
    return (x - 1) + "," + y;
}
testDir.push(testNorth);
setDir.push(setNorth);
//south
testSouth = function (x, y) {
    var south = false;
    for (let j = (y - 1); j <= (y + 1); j++) {
        south = south || elvesPos.includes((x + 1) + "," + j);
    }
    return south;
}
setSouth = function (x, y) {
    return (x + 1) + "," + y;
}
testDir.push(testSouth);
setDir.push(setSouth);
//west
testWest = function (x, y) {
    var west = false;
    for (let i = (x - 1); i <= (x + 1); i++) {
        west = west || elvesPos.includes(i + "," + (y - 1));
    }
    return west;
}
setWest = function (x, y) {
    return x + "," + (y - 1);
}
testDir.push(testWest);
setDir.push(setWest);
//est
testEst = function (x, y) {
    var est = false;
    for (let i = (x - 1); i <= (x + 1); i++) {
        est = est || elvesPos.includes(i + "," + (y + 1));
    }
    return est;
}
setEst = function (x, y) {
    return x + "," + (y + 1);
}
testDir.push(testEst);
setDir.push(setEst);


function Elf(x, y) {
    this.x = x;
    this.y = y;
    this.nextPos = "";
    this.setNext = function () {
        var it = 0;        
        //console.log(x+" "+y)
        const close = testDir.map(x => x(this.x,this.y));
        //console.log(close)
        var found = false;
        if (close.includes(true)){
        while ((!found)&&(it<4)){
            if (!close[(index+it)%4]){
                this.nextPos=setDir[(index+it)%4](this.x,this.y);
                found = true;
            }
            it++;
        }
    }
    }

    this.move = function () {
        if (this.nextPos != "") {
            if (elves.map(e => e.nextPos).filter(n => n == this.nextPos).length < 2) {
                const sp = this.nextPos.split(",");
                this.x = Number(sp[0]);
                this.y = Number(sp[1]);
            }
        }
    }

    this.stringPos = function () {
        return this.x + "," + this.y;
    }

}


print = function () {
    var xMin = Math.min(...elves.map(e => e.x));
    var xMax = Math.max(...elves.map(e => e.x));
    var yMin = Math.min(...elves.map(e => e.y));
    var yMax = Math.max(...elves.map(e => e.y));
    const elvesPos = elves.map(e => e.stringPos());
    for (let i = xMin; i <= xMax; i++) {
        for (let j = yMin; j <= yMax; j++) {
            if (elvesPos.includes(i + "," + j)) {
                process.stdout.write("#");
            } else {
                process.stdout.write(".");
            }
        }
        console.log("");
    }
}
allFileContents.split(/\r?\n/).forEach((line, x) => {
    if (line != "") {
        line.split('').forEach((char, y) => {
            if (char == '#') {
                elves.push(new Elf(x, y));
            }
        })
    }
})

//print();
elvesPos = elves.map(e => e.stringPos());
var before = elvesPos.sort().join("|");
var after = "";
for (let i=0;i<10;i++){
    elvesPos = elves.map(e => e.stringPos());
    elves.forEach(e => e.setNext());
    elves.forEach(e => e.move());
    //print();
    index++;
}
console.log((((Math.max(...elves.map(e => e.x))) - (Math.min(...elves.map(e => e.x))) + 1) * ((Math.max(...elves.map(e => e.y))) - (Math.min(...elves.map(e => e.y))) + 1)) - elves.length);

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start;
console.info('Execution time: %dms', end);