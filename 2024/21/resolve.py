from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

pad = [['7','8','9'],['4','5','6'],['1','2','3'],['x','0','A']]
rPad =[['x','^','A'],['<','v','>']]

#short path in first pad
paths = {}
#short path in robot pad
rPaths = {}

def getPaths(tmpX,tmpY,dX,dY,x2,y2,forbidden):
    if tmpX==x2 and tmpY==y2:
        return [""]
    res = []
    if dX!=0 and tmpX != x2 and (tmpX+dX != forbidden[0] or tmpY!=forbidden[1]):
        res += list(map(lambda st: ("<" if dX==-1 else ">")+st,getPaths(tmpX+dX,tmpY,dX,dY,x2,y2,forbidden)))
    if dY!=0 and tmpY != y2 and (tmpX != forbidden[0] or tmpY+dY!=forbidden[1]):
        res += list(map(lambda st: ("^" if dY==-1 else "v")+st,getPaths(tmpX,tmpY+dY,dX,dY,x2,y2,forbidden)))
    return res

def computePaths(padEntry,pathOut,forbidden):
    for y in range(0,len(padEntry)) :
        for x in range(0,len(padEntry[y])):
            c1 = padEntry[y][x]
            if c1!='x':
                for y2 in range(0,len(padEntry)):
                    for x2 in range(0,len(padEntry[y2])):
                        c2 = padEntry[y2][x2]
                        if (x!=x2 or y!=y2) and c2!='x':
                              dx = 0 if x==x2 else (x2-x)//abs(x2-x)
                              dy = 0 if y==y2 else (y2-y)//abs(y2-y)
                              pathOut[c1+c2]=getPaths(x,y,dx,dy,x2,y2,forbidden)
                        elif c2!='x':
                            pathOut[c1+c1]=[""]


computePaths(pad,paths,[0,3])
computePaths(rPad,rPaths,[0,0])



#robotStep
def robotStep(res):
    shortest = []
    shortestLen = -1
    run = []
    for s in res:
        run.append(["A"+s,""])
    while len(run)!=0:
        step = run[0]
        run = run[1:]
        if len(step[0])==1:
            l = len(step[1])
            if shortestLen == -1 or l<shortestLen:
                shortestLen=l
                shortest=[step[1]]
            elif l == shortestLen:
                shortest.append(step[1])
        else:
            tmp = step[0][1:]
            for p in rPaths[step[0][0:2]]:
                tmp2 = step[1]+p+'A'
                if shortestLen==-1 or len(tmp2)<=shortestLen:
                    run.insert(0,[tmp,tmp2])
    return shortest



finalRes = 0
for line in lines:
    print(line.strip("\n"))
    s = "A"+line.strip("\n")
    res = [""]
    for i in range(0,len(s)-1):
        tmpRes = []
        for p in paths[s[i]+s[i+1]]:
            tmpRes = tmpRes+list(map(lambda x : x+p+'A',res))
        res = tmpRes
    res = robotStep(res)
    res = robotStep(res)
    print(len(res[0]))
    print(int(s[1:-1]))
    finalRes+=len(res[0])*int(s[1:-1])
print(finalRes)


