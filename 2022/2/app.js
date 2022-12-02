const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');
var points = {"A":1,"B":2,"C":3,"X":1,"Y":2,"Z":3};
var gain = {"A":{"X":3,"Y":0,"Z":6},"B":{"X":6,"Y":3,"Z":0},"C":{"X":0,"Y":6,"Z":3},"X":{"A":3,"B":0,"C":6},"Y":{"A":6,"B":3,"C":0},"Z":{"A":0,"B":6,"C":3}};

var corresp = {"X":{"A":"Z","B":"X","C":"Y"},"Y":{"A":"X","B":"Y","C":"Z"},"Z":{"A":"Y","B":"Z","C":"X"}};

var player = 0;
var opponent = 0;
var playerV2 = 0;
var opponentV2 = 0;

allFileContents.split(/\r?\n/).forEach(line =>  {
  if (line!=""){
    console.log(line);
    const op = line.split(' ');
    console.log(points[op[1]]+gain[op[1]][op[0]]);
    player += points[op[1]]+gain[op[1]][op[0]];
    opponent += points[op[0]]+gain[op[0]][op[1]];
    const move = corresp[op[1]][op[0]];
    console.log(move);
    console.log(gain[move][op[0]]);
    playerV2 += points[move]+gain[move][op[0]];
    opponentV2 += points[op[0]]+gain[op[0]][move];
  }
});
console.log("player : "+player);
console.log("opponent : "+opponent);
console.log("version 2");
console.log("player : "+playerV2);
console.log("opponent : "+opponentV2);
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
