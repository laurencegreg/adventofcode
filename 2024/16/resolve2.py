from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

map =[]
start = []
end = []
pos = []
pathes = {}

for line in lines :
    map.append(list(line.strip('\n'))) 
    if "S" in line :
            y = len(map)-1
            start=[map[y].index('S'),y]
    if "E" in line :
            y = len(map)-1
            end=[map[y].index('E'),y]
def toStr (pos,stp):
    return str(pos)+','+str(stp)
def toArr (st):
    sp = st.split(',')
    return [[int(sp[0][1:]),int(sp[1][:-1])],[int(sp[2][1:]),int(sp[3][:-1])]]
#ways = [currentPoint,position,direction] orderer by points
passed = {toStr(start,[-1,0]):0}
pos.append(toStr(start,[-1,0]))
pathes[toStr(start,[-1,0])]={str(start)}
turns = {
    "-1,0":[[0,1],[0,-1]],
    "1,0":[[0,1],[0,-1]],
    "0,1":[[1,0],[-1,0]],
    "0,-1":[[1,0],[-1,0]]
}


res = -1
minVal = 0
while res == -1 or minVal<res :
    pos.sort(key=lambda name: passed[name])
    minKey = pos[0]
    pos=pos[1:]
    minVal = passed[minKey]
    curr = toArr(minKey)
    nextX = curr[0][0]+curr[1][0]
    nextY = curr[0][1]+curr[1][1]
    st = toStr([nextX,nextY],curr[1])
    if map[nextY][nextX]=='E':
        if not(st in passed) or passed[st]>minVal+1:
            passed[st]=minVal+1
            tmp = pathes[minKey].copy()
            tmp.add(str([nextX,nextY]))
            pathes[st]= tmp
            res=passed[st]
    else :
        if map[nextY][nextX]=='.':
            if not(st in passed) or passed[st]>minVal+1:
                passed[st]=minVal+1
                tmp = pathes[minKey].copy()
                tmp.add(str([nextX,nextY]))
                pathes[st]= tmp
                pos.append(st)
            elif st in passed and passed[st]==minVal+1:
                tmp = pathes[minKey].copy()
                tmp = tmp | pathes[st]
                pathes[st]= tmp
        for d in turns[str(curr[1][0])+','+str(curr[1][1])]:
            std = toStr(curr[0],d)
            if not(std in passed) or passed[std]>minVal+1000:
                passed[std]=minVal+1000
                pathes[std]=pathes[minKey].copy()
                pos.append(std)
            elif std in passed and passed[std]==minVal+1000:
                tmp = pathes[minKey].copy()
                tmp = tmp | pathes[std]
                pathes[std]= tmp
            
s = set()
for k in passed:
    if str(end) in k and  passed[k]==res:
        s = s | pathes[k]

for d in s :
    sp = d.split(',')
    map[int(sp[1][:-1])][int(sp[0][1:])]='O'

for l in map:
    print("".join(l))
print(len(s))