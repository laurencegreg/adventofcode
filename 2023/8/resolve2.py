from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

lr = {"L":0,"R":1}
dest = list(lines[0].strip('\n'))
dir = {}

for line in lines[2:] : 
    dir[line[0:3]]=[line[7:10],line[12:15]]


end = False
pos = list(filter(lambda x: x[2]=='A',dir.keys()))

ends = []
endPos = []
for pair in enumerate(pos) :
    idx,p = pair
    ends.append(list(map(lambda x : [],dest)))
    endPos.append(list(map(lambda x : [],dest)))
    it = 0
    end = False
    name = p
    while not end :
        name = dir[name][lr[dest[it%len(dest)]]]
        if name[2]=='Z':
            if name in ends[idx][it%len(dest)]:
                end = True
            else :
                endPos[idx][it%len(dest)].append(it+1)
                ends[idx][it%len(dest)].append(name)
        it+=1

def ppcm(a,b):
    p=a*b
    while(a!=b):
        if (a<b): b-=a
        else: a-=b
    return int(p/a)

for i in range(0,len(endPos[0])):
    empty = False
    for j in range(0,len(endPos)):
        empty = empty or len(endPos[j][i])==0
    if not empty :
        val = endPos[0][i][0]
        for k in range(1,len(endPos)):
            val = ppcm(val,endPos[k][i][0])

print(val)