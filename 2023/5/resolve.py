from operator import truediv
import re
f = open("input")
lines = f.readlines()
f.close()

corresp = {}
rangeMap = {}
seeds = map(int,lines[0].split(':')[1].strip().split(' '))

i=1
dest = ""
while i<len(lines) :
    if (lines[i]=="\n"):
        i+=1
        info = lines[i].split(' ')[0].split('-')
        corresp[info[0]]=info[2]
        dest=info[2]
        rangeMap[dest]=[]
    else :
        rangeMap[dest].append(map(int,lines[i].split(' ')))
    i+=1

def step(i,name):
    found = False
    res = i
    idx = 0
    rMap = rangeMap[name]
    while (not found and idx < len(rMap)):
        rStep = rMap[idx]
        if rStep[1]<=i and rStep[1]+rStep[2]>i :
            found = True
            res = rStep[0]+(i-rStep[1])
        idx+=1
    return res


lowest = -1
for seed in seeds :
    next = "seed"
    val = seed
    while next in corresp :
        next = corresp[next]
        val = step(val,next)
    lowest=val if (lowest==-1 or lowest>val) else lowest
print(lowest)
