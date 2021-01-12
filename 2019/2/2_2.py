import re
f = open("input")
lines = f.readlines()
f.close()

memory = list(map(int,lines[0].strip("\n").split(",")))

def compute(memory,noun,verb):  
    intCode = memory.copy()
    intCode[1]=noun
    intCode[2]=verb
    position = 0
    while intCode[position]<=2 :
        if intCode[position] == 1 :
            intCode[intCode[position+3]]=intCode[intCode[position+1]]+intCode[intCode[position+2]]
        elif intCode[position] == 2 :
            intCode[intCode[position+3]]=intCode[intCode[position+1]]*intCode[intCode[position+2]]
        position+=4
    if intCode[position]==99 :
        return intCode[0]
    else :
        return -1

for noun in range(0,100):
    for verb in range(0,100):
        if compute(memory,noun,verb)==19690720 :
            print(noun,verb,100*noun+verb)


