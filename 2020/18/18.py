import re
f = open("input")
lines = f.readlines()
f.close()

def calc (line,pos) :
    it = pos
    nextOp = None
    val = 0
    char = line[it]
    while it < len(line) and char !=  ")" :
        char = line[it]
        if char == '+' :
            nextOp = "add"
        elif char == '*' :
            nextOp = "mult"
        elif char.isdigit() or char == "(":
            x = 0
            if char.isdigit() :
                x = int(char)
            else :
                (x,it)=calc(line,it+1)
            if nextOp != None :
                if nextOp =="add" :
                    val += x
                    nextOp = None
                elif nextOp == "mult" :
                    val *= x
                    nextOp = None
            else :
                val = x
        it+=1
    if it < len(line) :
        if char == ")" :
            return (val,it-1)
        else:
            print("questufoula")
    else :
        return(val,it)

print(sum(list(map(lambda line : calc(line,0)[0],lines))))