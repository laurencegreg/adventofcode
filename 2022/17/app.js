const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

const rocks = new Set();
var highest = 0;
var moveDict = { '<': [0, -1], '>': [0,1] };
const line = allFileContents.split(/\r?\n/)[0];
var ind = 0;

function union(setA, setB) {
    let _union = new Set(setA);
    for (let elem of setB) {
        _union.add(elem);
    }
    return _union;
}

print = function (printed,tall) {
    console.log();
    for (let i = tall; i > 0; i--) {
        process.stdout.write("|");
        for (let j = 0; j < 7; j++) {
            if (printed.has(i + "," + j)) {
                process.stdout.write("#");
            } else {
                process.stdout.write(".");
            }
        }
        console.log('|');
    }
    console.log("+-------+");
    console.log();
}

contact = function (pos) {
    return (rocks.has(pos.join()) || (pos[1] < 0) || (pos[1] >= 7) || (pos[0] <= 0));
}

function Piece(pattern) {
    const start = [highest + 4, 0];

    this.pattern = pattern.map(p => p.map((x, i) => x + start[i]));

    this.moveDown = function () {
        //console.log("moveDown");
        const mv = [-1, 0];
        const tmp = this.pattern.map(p => p.map((x, i) => x + mv[i]));
        if (tmp.map(p => contact(p)).reduce((a, c) => (a || c), false)) {
            this.pattern.forEach(p => {
                if (highest < p[0]) {
                    highest = p[0];
                }
                rocks.add(p.join());
            })
            //print(union(rocks,new Set(this.pattern.map(x=>x.join()))),10);
        } else {
            this.pattern = tmp;
            //print(union(rocks,new Set(this.pattern.map(x=>x.join()))),10);
            this.moveH();
        }
        
    }

    this.moveH = function () {
        //console.log("moveH")
        const mv = moveDict[line[ind]];
        const tmp = this.pattern.map(p => p.map((x, i) => x + mv[i]));
        if (!tmp.map(p => contact(p)).reduce((a, c) => (a || c), false)) {
            this.pattern = tmp;
            //print(union(rocks,new Set(this.pattern.map(x=>x.join()))),10);
        }//else{
        //    print(union(rocks,new Set(this.pattern.map(x=>x.join()))),10);
        //}
        
        ind = (ind + 1) % (line.length);
        this.moveDown();
    }
}

function PieceCreator() {
    this.shape = [
        [[0, 2], [0, 3], [0, 4], [0, 5]],
        [[2, 3], [1, 2], [1, 3], [1, 4], [0, 3]],
        [[2, 4], [1, 4], [0, 2], [0, 3], [0, 4]],
        [[0, 2], [1, 2], [2, 2], [3, 2]],
        [[0, 2], [0, 3], [1, 2], [1, 3]]];

    this.index = 0;

    this.create = function () {
        const piece = new Piece([...this.shape[this.index]]);
        this.index = (this.index + 1) % 5;
        return piece;
    }
}

const pc = new PieceCreator();

for (let i = 0; i < 2022; i++) {
    const p = pc.create();
    //print(union(rocks,new Set(p.pattern.map(x=>x.join()))),10);
    p.moveH();
}

console.log("part 1 : " + highest);
//print(rocks,10);
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start;
console.info('Execution time: %dms', end);