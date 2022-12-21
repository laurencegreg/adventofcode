const fs = require('fs');
const util = require('util');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
ind = 0;
monkeys = {}
allFileContents.split(/\r?\n/).forEach(line => {
    if (line != '') {
        const sp = line.split(' ');
        const monkName = sp[0].slice(0, -1);
        if (sp.length > 2) {
            const op = sp[2];
            const m1 = sp[1];
            const m2 = sp[3];
            if (monkName == "root") {
                monkeys["root"] = function () { return monkeys[m1]() == monkeys[m2]() }
                monkeys["rootLeft"] = function () { return monkeys[m1]() }
                monkeys["rootRight"] = function () { return monkeys[m2]() }
            } else {
                switch (op) {
                    case '+':
                        monkeys[monkName] = function () { return monkeys[m1]() + monkeys[m2]() };
                        break;
                    case '*':
                        monkeys[monkName] = function () { return monkeys[m1]() * monkeys[m2]() };
                        break;
                    case '-':
                        monkeys[monkName] = function () { return monkeys[m1]() - monkeys[m2]() };
                        break;
                    case '/':
                        monkeys[monkName] = function () { return monkeys[m1]() / monkeys[m2]() };
                        break;
                }
            }
        } else {
            const num = Number(sp[1])
            monkeys[monkName] = function () { return num };
        }
    }
});

var step = 1;
monkeys["humn"] = function () { return step };
const target = monkeys["rootRight"]();
var left = monkeys["rootLeft"]();
while (left > target) {
    step *= 10;
    monkeys["humn"] = function () { return step };
    left = monkeys["rootLeft"]();
}

var humanUp = step;
var humanDown = step;
while (!monkeys["root"]()) {
    humanDown = humanUp;
    step /= 10;
    monkeys["humn"] = function () { return humanDown };
    left = monkeys["rootLeft"]();
    while (left < target) {
        humanUp = humanDown;
        humanDown -= step;
        monkeys["humn"] = function () { return humanDown };
        left = monkeys["rootLeft"]();
    }
}
console.log("step 2 : " + monkeys["humn"]())

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start;
console.info('Execution time: %dms', end);