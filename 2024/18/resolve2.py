from collections import Counter
import math
f = open("input")
lines = f.readlines()
f.close()

startRegisters = {}
ops = []
for line in lines :
    if "Register" in line:
        sp = line.strip('\n').split(" ")
        startRegisters[sp[1][:-1]]=int(sp[2])
    elif ',' in line:
        target=line.strip('\n').split(" ")[1]
        ops=list(map(int,line.strip('\n').split(" ")[1].split(',')))

#target="2,4,1,2,7,5,0,3,4,7,1,7,5,5,3,0,"
min=1*3
max=2*3+2
print(target)
#A = A //3//3 after 1 loop
for i in range(0,len(list(target.split(',')))-2):
    max=(max*3+2)*3+2
    min=min*3*3
print("A is between "+str(min)+" and "+str(max))
target+=","
print(target)
#j=startRegisters['A']
j=1
aStr = ""
print(j)
output=""
while output!=target:  
    i=0
    registers = {'A':int(str(bin(j))[2:]+aStr,2),'B':0,'C':0}
    #registers = {'A':j,'B':0,'C':0}
    output=""
    while i < len(ops) and target.startswith(output):
        op = ops[i]
        literal = ops[i+1]
        combo = literal
        if combo > 3:
            if combo == 4:
                combo = registers['A']
            elif combo == 5:
                combo = registers['B']
            elif combo == 6:
                combo = registers['C']
        if op == 0:
            registers['A']=registers['A']//int(math.pow(2, combo))
        elif op == 1:
            registers['B']=registers['B']^literal
        elif op ==2:
            registers['B']=combo%8
        elif op ==3:
            if registers['A']!=0:
                i=literal-2
        elif op ==4:
            registers['B']=registers['B']^registers['C']
        elif op == 5:
            output += str(combo%8)+","
        elif op == 6:
            registers['B']=registers['A']//int(math.pow(2, combo))
        elif op == 7:
            registers['C']=registers['A']//int(math.pow(2, combo))
        i+=2
    if target.startswith(output):
        print(output)
        aStr=str(bin(j))[2:]+aStr
        print(aStr)
        j=1
    else:
        j+=1