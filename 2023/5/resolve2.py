from operator import truediv
import re
f = open("input")
lines = f.readlines()
f.close()

corresp = {}
rangeMap = {}
seeds = map(int,lines[0].split(':')[1].strip().split(' '))
seedsPart = []
for i in range(0,len(seeds),2):
    seedsPart.append([seeds[i],seeds[i]+seeds[i+1]-1])
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

def step(ar,name):
    found = False
    idx = 0
    rMap = rangeMap[name]
    tmpStep = []
    tmpInit = ar
    while idx < len(rMap):
        tmpTrans = []
        rStep = rMap[idx]
        r = rMap[idx]
        min = rStep[1]
        max = rStep[1]+rStep[2]-1
        for ran in tmpInit:
            over = overlap(ran,[min,max])
            for overAr in over[1]:
                tmpStep.append(map(lambda x: x+(rStep[0]-rStep[1]),overAr))
            tmpTrans+=over[0]
        tmpInit=tmpTrans
        idx+=1
    return tmpStep+tmpInit
        

# return 2 array with first array range out of target and in second range in target
def overlap(pair,target):
    tmp= [[],[]]
    min = target[0]
    max = target[1]
    mini = pair[0]
    maxi = pair[1]
    if maxi<min or mini>max:
        tmp[0].append([mini,maxi])
    else : 
        if mini>=min and mini<=max :
            if maxi > max : 
                tmp[0].append([max+1,maxi])
                tmp[1].append([mini,max])
            else :
                tmp[1].append([mini,maxi])
        else :
            if maxi>=min and maxi<=max :
                tmp[0].append([mini,min-1])
                tmp[1].append([min,maxi])
            else :
                tmp[0].append([mini,min-1])
                tmp[1].append([min,max])
                tmp[0].append([max+1,maxi])
    return tmp


#seedsPart = [seedsPart[1]]
next = "seed"
while next in corresp :
    next = corresp[next]
    seedsPart=step(seedsPart,next)
print(min(map(lambda x : x[0],seedsPart)))