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
    while i<len(line)-1:
        if line[i] in lasts : 
            if len(set(line[i+1:])&set(lasts[line[i]]))!=0:
                ok = False
                num = line.pop(i)
                j = i
                while len(set(line[j:])&set(lasts[num]))!=0 :
                    j+=1
                line.insert(j,num)
                i=-1
        i+=1
    if not(ok):
        res += int(line[len(line)//2])

print(res)