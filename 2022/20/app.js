const fs = require('fs');
const util = require('util');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
ind = 0;
Node = function (str) {
    this.ind = ind;
    ind++;
    this.value = Number(str);
    this.next = null;
    this.previous = null;

    this.print = function () {
        console.log("////// node " + this.ind + "///////");
        console.log("value " + this.value);
        console.log("previous : " + this.previous.ind + "/" + this.previous.value);
        console.log("next : " + this.next.ind + "/" + this.next.value)

    }

    this.forward = function () {
        const n = this.next;
        const p = this.previous;
        n.previous = p;
        p.next = n;
        n.next.previous = this;
        this.previous = this.next;
        this.next = n.next;
        n.next = this;
    }

    this.backward = function () {
        const n = this.next;
        const p = this.previous;
        n.previous = p;
        p.next = n;
        p.previous.next = this;
        this.previous = p.previous;
        this.next = p;
        p.previous = this;
    }
}
var first = null;
var prev = null;
var zero = null;
const lines = allFileContents.split(/\r?\n/);

var coords = lines.forEach((x, i) => {
    if (x != '') {
        const n = new Node(x);
        if (first == null) {
            first = n;
        } else {
            n.previous = prev;
            prev.next = n;
        }
        if (x == 0) {
            zero = n;
        }
        prev = n;
    }
});
prev.next = first;
first.previous = prev;

var current = first;
for (let i = 0; i < lines.length - 1; i++) {
    while (current.ind != i) {
        current = current.next;
    }
    const moving = current;
    var steps = moving.value;
    while (steps != 0) {
        if (steps > 0) {
            moving.forward();
            steps--;
        } else {
            moving.backward();
            steps++;
        }
    }
}

const res = []
var parkour = zero;
for (let i = 0; i < lines.length; i++) {
    res.push(parkour.value);
    parkour = parkour.next;
}

console.log("step 1 : " + (res[1000 % res.length] + res[2000 % res.length] + res[3000 % res.length]));
// printed = first;
// for (i=0;i<lines.length;i++){
//    printed.print();
//    printed = printed.next;
// }
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start;
console.info('Execution time: %dms', end);