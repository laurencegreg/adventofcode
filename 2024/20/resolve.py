from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

empty= []
emptySt= []
minPath={}
compute = []
height = len(lines)
width = len(lines[0])-1
for y in range(0,len(lines)) :
    line = lines[y].strip('\n')
    for x in range(0,len(line)):
        if line[x]!='#':
            emptySt.append(str([x,y]))
            empty.append([x,y])
        if line[x]=='E':
            minPath[str([x,y])]=0
            compute.append([[x,y],0])

dir = [[0,1],[1,0],[-1,0],[0,-1]]
while len(compute)>0:
    p = compute[0]
    compute = compute[1:]
    for d in dir:
        x=p[0][0]+d[0]
        y=p[0][1]+d[1]
        if 0<=x<width and 0<=y<height and str([x,y]) in emptySt and (not str([x,y]) in minPath or minPath[str([x,y])]>p[1]+1):
            minPath[str([x,y])]=p[1]+1
            compute.append([[x,y],p[1]+1])

res={}
cheatDir = [[0,2],[-2,0],[2,0],[0,-2],[1,1],[1,-1],[-1,1],[-1,-1]]
for e in empty:
    for d in cheatDir:
        x=e[0]+d[0]
        y=e[1]+d[1]
        next = minPath[str(e)]-2
        if str([x,y]) in minPath and next>minPath[str([x,y])]:
            diff = next-minPath[str([x,y])]
            if diff in res :
                res[diff]+=1
            else:
                res[diff]=1

fin = 0
for x in [x for x in res if x>=100]:
    fin+=res[x]

print(fin)