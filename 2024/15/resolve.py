from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

map =[]
path = []
pos = []

for line in lines :
    if "#" in line :
        map.append(list(line.strip('\n'))) 
        if "@" in line :
            y = len(map)-1
            pos=[map[y].index('@'),y]
    elif line != "\n":
        path += list(line.strip('\n'))

dir = {'>':[1,0],'^':[0,-1],'<':[-1,0],'v':[0,1]}

for step in path:
    d = dir[step]
    next = [pos[0]+d[0],pos[1]+d[1]]
    if map[next[1]][next[0]]==".":
        map[pos[1]][pos[0]]="."
        map[next[1]][next[0]]="@"
        pos=next
    elif map[next[1]][next[0]]=="O":
        tmp = next.copy()
        while map[tmp[1]][tmp[0]]=="O":
            tmp = [tmp[0]+d[0],tmp[1]+d[1]]
        if map[tmp[1]][tmp[0]]==".":
            map[pos[1]][pos[0]]="."
            map[next[1]][next[0]]="@"
            map[tmp[1]][tmp[0]]="O"
            pos=next
for l in map:
    print("".join(l))

res = 0
for y in range(0,len(map)):
    for x in range(0,len(map[y])):
        if map[y][x]=='O':
            res += 100*y+x
print(res)