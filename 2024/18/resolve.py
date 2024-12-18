from collections import Counter
import math
f = open("input")
lines = f.readlines()
f.close()
limit = 70
maxSteps = limit*limit
end = str([limit,limit])
pos = {}
pos[str([0,0])]=0
dirs = [[0,1],[0,-1],[1,0],[-1,0]]
for i in range(0,1024):
    pos["["+lines[i].strip('\n').replace(",",", ")+"]"]=-1
run = [[[0,0],0]]
steps = 0
while len(run)!=0:
    p = run[0]
    run = run[1:]
    for d in dirs :
            x = p[0][0]+d[0]
            y = p[0][1]+d[1]
            pn = [x,y]
            st = p[1]+1
            if 0<=x<=limit and 0<=y<=limit and st<maxSteps and (not(str((pn)) in pos) or pos[str(pn)]>st):
                print([pn,st])
                run.insert(0,[pn,st])
                pos[str(pn)]=st
            if str(pn)==end:
                 maxSteps=pos[end]

print(pos[str(end)])