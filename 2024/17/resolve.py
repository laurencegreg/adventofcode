from collections import Counter
import math
f = open("input")
lines = f.readlines()
f.close()

registers = {}
ops = []
for line in lines :
    if "Register" in line:
        sp = line.strip('\n').split(" ")
        registers[sp[1][:-1]]=int(sp[2])
    elif ',' in line:
        ops=list(map(int,line.strip('\n').split(" ")[1].split(',')))
                 
i=0
output=""
while i < len(ops):
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
print(output[:-1])
