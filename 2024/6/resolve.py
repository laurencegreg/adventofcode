from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

plan = []
posX = 0
posY = 0
found = False
for line in lines :
    if '^' in line :
       posY=line.find('^')
       found=True
    if not(found) :
        posX+=1
    plan.append(list(line.strip('\n')))

dirX = -1
dirY = 0

posSet = set()
while 0<=posX<len(plan) and 0<=posY<len(plan[posY]):
    posSet.add(str(posX)+','+str(posY))
    while 0<=posX+dirX<len(plan) and 0<=posY+dirY<len(plan) and plan[posX+dirX][posY+dirY] == '#':
        #1 0 -> 0 -1 -> -1 0 -> 0 1
        if dirX == 0 : 
            dirX = dirY
            dirY = 0
        else : 
            dirY = -dirX
            dirX = 0
    posX +=dirX
    posY +=dirY

print(len(posSet))