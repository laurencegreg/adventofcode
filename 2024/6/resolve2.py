from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

plan = []
startPosX = 0
startPosY = 0
found = False
for line in lines :
    if '^' in line :
       startPosY=line.find('^')
       found=True
    if not(found) :
        startPosX+=1
    plan.append(list(line.strip('\n')))


def run(newPlan,pX,pY):
    posX = pX
    posY = pY
    dirX = -1
    dirY = 0
    dirPosSet = set()
    posString = str(posX)+','+str(posY)+','+str(dirX)+','+str(dirY)
    while 0<=posX<len(newPlan) and 0<=posY<len(newPlan[posX]) and not(posString in dirPosSet):
        dirPosSet.add(posString)
        while 0<=posX+dirX<len(newPlan) and 0<=posY+dirY<len(newPlan) and newPlan[posX+dirX][posY+dirY] == '#':
            #1 0 -> 0 -1 -> -1 0 -> 0 1
            if dirX == 0 : 
                dirX = dirY
                dirY = 0
            else : 
                dirY = -dirX
                dirX = 0
        posX +=dirX
        posY +=dirY
        posString = str(posX)+','+str(posY)+','+str(dirX)+','+str(dirY)
    return posString in dirPosSet

res = 0
for i in range (0,len(plan)):
    for j in range (0,len(plan[i])):
        if plan[i][j]=='.':
            newPlan = list(map(lambda x : x.copy(),plan))
            newPlan[i][j]='#'
            if run(newPlan,startPosX,startPosY):
                print(str(i)+","+str(j))
                res+=1
print(res)