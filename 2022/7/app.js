const fs = require('fs');
var start = new Date();
const allFileContents = fs.readFileSync('input', 'utf-8');

function Dir(name,parent) {

    this.name = name;
    this.parent = parent;
    this.size = 0;
    this.files={};
    this.dirs={};
    this.globalSize = 0
    
    //add a file and it size to dir
    this.addFile = function(fileName,size) {
        this.files[fileName]=size;
    }

    //add a new dir in this dir
    this.addDir = function(dirName){
        this.dirs[dirName]=new Dir(dirName,this);
    }

    //go to dir dirName
    this.cd = function(dirName){
        return this.dirs[dirName];
    }

    //cd ..
    this.back = function(){
        return this.parent;
    }

    //print dir content
    this.ls = function(){
        console.log("ls "+this.name)
        for (const [key, value] of Object.entries(this.dirs)) {
            console.log(`- ${key} (dir)`);
        }
        for (const [key, value] of Object.entries(this.files)) {
            console.log(`- ${key} (file, size=${value})`);
          }
    }

    //compute full size of this dir if not already done
    this.fullSize = function(){
        if(this.globalSize==0){
            var sum = 0;
            for (const [key, value] of Object.entries(this.dirs)) {
                sum += value.fullSize();
            }
            for (const [key, value] of Object.entries(this.files)) {
                sum+=value;
            }
            this.globalSize = sum;
        }
        return this.globalSize;
    }

    //part 1 resolver. Add size (if <= 100000) of this dir and the sumUp of all sub dirs
    this.sumUp = function(){
        var sum = 0;
        const full = this.fullSize();
        if (full<=100000){
            sum+=full
        }

        for (const [key, value] of Object.entries(this.dirs)) {
            sum += value.sumUp();
        }
        return sum;
    }

    //part 2 resolver. Search the minimal dir in this dir and all his sub dir greater than needed space
    this.findSpace = function(needed){
        if(this.fullSize()<needed){
            return null
        }else{
            var minSpace = this.fullSize()
            for (const [key, value] of Object.entries(this.dirs)) {
                const minDir = value.findSpace(needed);
                if ((minDir!=null)&&(minDir<minSpace)){
                    minSpace=minDir;
                }
            }
            return minSpace;
        }
    }
}

//dirs filling
const root = new Dir("root",null)
var current = root
allFileContents.split(/\r?\n/).forEach(line =>  {
  if ((line!="")&&(line!="$ cd /")){
    const splitted = line.split(' ');
    if(splitted[0]=='$'){
        if (splitted[1]=="cd"){
            if (splitted[2]==".."){
                current = current.back();
            }else{
                current = current.cd(splitted[2]);
            }
        }
    }else{
       if (splitted[0]=="dir"){
           current.addDir(splitted[1])
       }else{
           current.addFile(splitted[1],Number(splitted[0]))
       }
    }
  }
});

//part 1
console.log("step 1 : "+root.sumUp())

//part 2
const needSpace = 30000000-(70000000-root.fullSize())
console.log("step 2 :");
console.log(`need ${needSpace} space`)
console.log(`deleted dir size : ${root.findSpace(needSpace)}`);

const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);
var end = new Date() - start
console.info('Execution time: %dms', end)
