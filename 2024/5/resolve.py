from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

firsts = {}
lasts = {}
checkLists = []
for line in lines :
    if '|' in line :
        sp = line.strip('\n').split("|")
        if sp[0] in firsts :
            firsts[sp[0]].append(sp[1])
        else :
            firsts[sp[0]]=[sp[1]]
        if sp[1] in lasts :
            lasts[sp[1]].append(sp[0])
        else :
            lasts[sp[1]]=[sp[0]]
    if ',' in line :
        checkLists.append(line.strip('\n').split(","))


res = 0
for line in checkLists:
    i = 0
    ok = True
    while i<len(line)-1 and ok :
        if line[i] in lasts : 
            ok = len(set(line[i+1:])&set(lasts[line[i]]))==0
        i+=1
    if ok : 
        res += int(line[len(line)//2])

print(res)