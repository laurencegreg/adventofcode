from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

robots = []
for line in lines :
    sp = line.strip("\n").split(" ")
    p = list(map(int,sp[0].split('=')[1].split(',')))
    v = list(map(int,sp[1].split('=')[1].split(',')))
    robots.append([p,v])

maxX = 101
maxY = 103
seconds = 100
def move(robot):
    return [(robot[0][0]+seconds*robot[1][0])%maxX,(robot[0][1]+seconds*robot[1][1])%maxY]

finalPos = list(map(move,robots))

res = 1
tmp = 0
for x in range(0,maxX//2):
    for y in range(0,maxY//2):
        for r in finalPos:
            if r[0]==x and r[1]==y:
                tmp+=1
print(tmp)
res *= tmp
    
tmp = 0
for x in range(0,maxX//2):
    for y in range(maxY//2+1,maxY):
        for r in finalPos:
            if r[0]==x and r[1]==y:
                tmp+=1
print(tmp)
res *= tmp
tmp = 0
for x in range(maxX//2+1,maxX): 
    for y in range(0,maxY//2):
        for r in finalPos:
            if r[0]==x and r[1]==y:
                tmp+=1
print(tmp)
res *= tmp
tmp = 0
for x in range(maxX//2+1,maxX):
    for y in range(maxY//2+1,maxY):
        for r in finalPos:
            if r[0]==x and r[1]==y:
                tmp+=1
print(tmp)
res *= tmp

print(res)