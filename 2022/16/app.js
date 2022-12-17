const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

var valvesDict = {};
var globalValves = [];
function Valve(id, rate, valves) {

    this.id = id;
    this.valves = valves;
    this.distValves = {};
    this.rate = rate;
    valvesDict[id] = globalValves.length;
    globalValves.push(this);

    this.run = function (openned, nbStep) {
        var res = 0;
        if (nbStep == 0) {
            return res;
        }
        res = gain(openned)*nbStep;
        if (!openned.includes(this.id)) {
            const temp = gain(openned) + this.run([...openned, this.id], nbStep - 1);
            if (temp > res) {
                res = temp;
            }
        } else {
            Object.entries(this.distValves).forEach(x => {
                if ((!openned.includes(x[0]))&&(nbStep>=x[1])) {
                    const temp = gain(openned) * x[1] + globalValves[valvesDict[x[0]]].run([...openned], nbStep - x[1]);
                    if (temp > res) {
                        res = temp;
                    }
                }
            })
        }
        return res;
    }


}

gain = function (openValves) {
    var res = 0;
    return openValves.map(x => globalValves[valvesDict[x]].rate).reduce((acc, curr) => acc + curr, res);
}

allFileContents.split(/\r?\n/).forEach(line => {
    if (line != "") {
        const lineRe = new RegExp('Valve ([A-Z]+) has flow rate=(\\d+); tunnels? leads? to valves? ([A-Z, ]+)', 'g');
        const extract = lineRe.exec(line);
        new Valve(extract[1], Number(extract[2]), extract[3].split(", "));
    }
})
//console.log(valvesDict);
//console.log(globalValves);
const usefull = globalValves.filter(x => (x.rate > 0));
const dist = Array.from({ length: globalValves.length }, e => Array(globalValves.length).fill(globalValves.length));
globalValves.forEach(valve => {
    const id = valvesDict[valve.id];
    dist[id][id] = 0;
    valve.valves.forEach(x => {
        dist[id][valvesDict[x]] = 1;
    })
})
var step = 1;
while ((dist.filter(ar => ar.includes(globalValves.length)).length > 0) && (step < dist.length)) {
    step++;
    for (let i = 0; i < dist.length; i++) {
        for (let j = 0; j < dist[i].length; j++) {
            const c = dist[i][j];
            if ((c < step) && (c > 0)) {
                for (let k = 0; k < dist[j].length; k++) {
                    const r = c + dist[j][k];
                    if ((r <= step) && (r < dist[i][k])) {
                        dist[i][k] = r;
                    }
                }
            }
        }
    }
}

usefull.forEach(v => {
    usefull.map(x => x.id).forEach(x => {
        if (x != v.id) {
            v.distValves[x] = dist[valvesDict[v.id]][valvesDict[x]];
        }
    })
})
const init = globalValves[valvesDict["AA"]];
usefull.map(x => x.id).forEach(x => {
    if (x != init.id) {
        init.distValves[x] = dist[valvesDict[init.id]][valvesDict[x]];
    }
})
console.log(init.run(['AA'],30))

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)