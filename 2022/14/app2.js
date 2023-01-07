const fs = require('fs');
const util = require('util')
var startDate = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

var lines = allFileContents.split(/\r?\n/);
var pos = new Set();
var lower = 0;
for (const line of lines) {
    if (line != "") {
        const rocks = line.split("->").map(x => x.trim().split(",").map(y => Number(y)));
        for (let i = 0; i < rocks.length - 1; i++) {
            if (rocks[i][0] == rocks[i + 1][0]) {
                const x = rocks[i][0]
                const start = rocks[i][1] > rocks[i + 1][1] ? rocks[i + 1][1] : rocks[i][1];
                const end = rocks[i][1] < rocks[i + 1][1] ? rocks[i + 1][1] : rocks[i][1];
                lower = lower < end ? end : lower;
                for (let y = start; y <= end; y++) {
                    pos.add(x + "," + y)
                }
            } else {
                const y = rocks[i][1]
                lower = lower < y ? y : lower;
                const start = rocks[i][0] > rocks[i + 1][0] ? rocks[i + 1][0] : rocks[i][0];
                const end = rocks[i][0] < rocks[i + 1][0] ? rocks[i + 1][0] : rocks[i][0];
                for (let x = start; x <= end; x++) {
                    pos.add(x + "," + y)
                }
            }
        }
    }
}
lower += 2;
const sandSource = [500, 0];
var flow = false;
var count = 0;
while (!flow) {
    if (pos.has(sandSource[0] + "," + sandSource[1])) {
        flow = true
    } else {
        var sx = sandSource[0];
        var sy = sandSource[1] + 1;
        var stop = false;
        while (!stop) {
            if (pos.has(sx + "," + sy) || (sy == lower)) {
                if (pos.has((sx - 1) + "," + sy) || (sy == lower)) {
                    if (pos.has((sx + 1) + "," + sy) || (sy == lower)) {
                        pos.add(sx + "," + (sy - 1));
                        stop = true;
                        count++;
                    } else {
                        sx++;
                        sy++;
                    }
                } else {
                    sx--;
                    sy++;
                }
            } else {
                sy++;

            }
        }
    }
}
console.log("part 2 : " + count);
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - startDate
console.info('Execution time: %dms', end)