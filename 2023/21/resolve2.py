from collections import Counter
import re
f = open("input.test")
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

lPlan = len(plan) 
wPlan = len(plan[0])

step = 5000
while step>0:
    tmpPoints = []
    for p in points :
        pU = [p[0]-1,p[1]]
        if not(pU in tmpPoints) and not (pU in points) and plan[pU[0]%lPlan][pU[1]%wPlan] != '#' :
            tmpPoints.append(pU)
        pD = [p[0]+1,p[1]]
        if not(pD in tmpPoints) and not (pD in points) and plan[pD[0]%lPlan][pD[1]%wPlan] != '#' :
            tmpPoints.append(pD)
        pL = [p[0],p[1]-1]
        if not(pL in tmpPoints) and not (pL in points) and plan[pL[0]%lPlan][pL[1]%wPlan] != '#' :
            tmpPoints.append(pL)
        pR = [p[0],p[1]+1]
        if not(pR in tmpPoints) and not (pR in points) and plan[pR[0]%lPlan][pR[1]%wPlan] != '#' :
            tmpPoints.append(pR)
    points = tmpPoints
    step-=1
print(len(points))