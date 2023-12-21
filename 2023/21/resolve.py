from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

plan = []
points = []
for i,line in enumerate(lines) : 
    sp = list(line.strip('\n'))
    if 'S' in sp:
        points.append([i,sp.index('S')])
        sp[sp.index('S')]='.'
    plan.append(sp)


step = 64
while step>0:
    tmpPoints = []
    for p in points :
        pU = [p[0]-1,p[1]]
        if not(pU in tmpPoints) and pU[0]>=0 and not (pU in points) and plan[pU[0]][pU[1]] != '#' :
            tmpPoints.append(pU)
        pD = [p[0]+1,p[1]]
        if not(pD in tmpPoints) and pD[0]<len(plan) and not (pD in points) and plan[pD[0]][pD[1]] != '#' :
            tmpPoints.append(pD)
        pL = [p[0],p[1]-1]
        if not(pL in tmpPoints) and pL[1]>=0 and not (pL in points) and plan[pL[0]][pL[1]] != '#' :
            tmpPoints.append(pL)
        pR = [p[0],p[1]+1]
        if not(pR in tmpPoints) and pR[1]<len(plan[pR[0]]) and not (pR in points) and plan[pR[0]][pR[1]] != '#' :
            tmpPoints.append(pR)
    points = tmpPoints
    step-=1
print(len(points))