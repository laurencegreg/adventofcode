const fs = require('fs');
const util = require('util')
var startDate = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

var lines = allFileContents.split(/\r?\n/);
//control : 0 if ok, 1 if ko, 2 if same
control = function(leftElt,rightElt){
    //console.log("control %O and %O",leftElt,rightElt);
    var lefty = leftElt;
    var righty = rightElt;
    if (Array.isArray(leftElt)){
        if (!Array.isArray(rightElt)){
            righty = [rightElt];
        }
    }else{
        if (!Array.isArray(rightElt)){
            if (leftElt == rightElt){
                return 2;
            }else{
                return leftElt>rightElt?1:0;
            }
        }else{
            lefty = [leftElt];
        }
    }

    var i = 0;
    var res = 2;
    while ((i<lefty.length) && (i<righty.length) && (res == 2)){
        res = control(lefty[i],righty[i]);
        i++;
    }
    if (res !=2){
        return res;
    }else{
        if (lefty.length == righty.length){
            return 2;
        }else{
            return (lefty.length > righty.length)?1:0;
        }
    }
}

getArr = function(str){
    return getArray(str)[0];
}
getArray = function(str){
    if(str[0]=="["){
        var r = getArray(str.slice(1));
        var arr = new Array();
        if (r[0]!=null){
            arr.push(r[0]);
        }
        if (r[1]!=null){
            while (r[1][0]==","){
                r = getArray(r[1].slice(1));
                arr.push(r[0]);
            }
        }
        return [arr,r[1].slice(1)];
    }else if (str[0]=="]"){
        return new Array (null,str);
    }else {
        const i = str.indexOf(",");
        const j = str.indexOf("]");
        if ((i!=-1)&&(i<j)){
            return [Number(str.slice(0,i)),str.slice(i)];
        }else{
            return [Number(str.slice(0,j)),str.slice(j)];
        }
    }
}

var ind = 1;
var it = 0;
var res = 0;
var packets = [];
const point1 = [[2]];
const point2 = [[6]];
packets.push(point1);
packets.push(point2);
while (it < lines.length){
    const left = getArr(lines[it]);
    packets.push(left);
    const right = getArr(lines[it+1]);
    packets.push(right);
    //console.log(`== Pair ${ind} ==`)
    //console.log(util.inspect(left, { maxArrayLength: null,breakLength: Infinity,depth: Infinity}));
    //console.log(util.inspect(right, { maxArrayLength: null,breakLength: Infinity,depth: Infinity}));
    if(control(left,right)==0){
        //console.log("right order")
        res+=ind;
    }else{
        //console.log("wrong order")
    }
    ind+=1;
    it+=3;
}

tribulle = function(arrays){
    var changed = true;
    var step = 0;
    while (changed){
        changed = false;
        step += 1;
        for (let i=0;i<(arrays.length-step);i++){
            if (control(arrays[i],arrays[i+1])!=0){
                changed=true;
                var temp = arrays[i];
                arrays[i] = arrays[i+1];
                arrays[i+1]=temp;
            }
        }
    }
    return arrays
}


console.log("part 1 : "+res);
const resPackets = tribulle(packets);
console.log("part 2 : "+(resPackets.indexOf(point1)+1)*(resPackets.indexOf(point2)+1));

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - startDate
console.info('Execution time: %dms', end)