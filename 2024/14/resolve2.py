from collections import Counter
import re
import sys
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

def move(robot):
    return [[(robot[0][0]+robot[1][0])%maxX,(robot[0][1]+robot[1][1])%maxY],robot[1]]

def printRobots(robots):
    grid = []
    for y in range(0,maxY):
        grid.append(['.']*maxX)
    for r in robots:
        grid[r[0][1]][r[0][0]]='#'
    for g in grid :
        print("".join(g))

printRobots(robots)
i=0
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    pos = set()
    while (len(pos)!=len(robots)) :
        robots=list(map(move,robots))
        pos = set()
        for r in robots :
            pos.add(str(r[0][0])+","+str(r[0][1]))
        i+=1
    print("-----")
    printRobots(robots)
    print(i)