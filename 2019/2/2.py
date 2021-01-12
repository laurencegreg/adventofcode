import re
f = open("input")
lines = f.readlines()
f.close()

intCode = list(map(int,lines[0].strip("\n").split(",")))
intCode[1]=12
intCode[2]=2
print(intCode)
position = 0
while intCode[position]<=2 :
    if intCode[position] == 1 :
        intCode[intCode[position+3]]=intCode[intCode[position+1]]+intCode[intCode[position+2]]
    elif intCode[position] == 2 :
        intCode[intCode[position+3]]=intCode[intCode[position+1]]*intCode[intCode[position+2]]
    position+=4

print(intCode)
