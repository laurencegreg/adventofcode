from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()


i = 0
pos = {}
for line in lines :
    arr = list(line.strip('\n'))
    for j in range(0,len(line)-1):
        if arr[j]!='.':
            if arr[j] in pos :
                pos[arr[j]].add(str(i)+','+str(j))
            else :
                pos[arr[j]]={str(i)+','+str(j)}
    i+=1
limX = (len(lines))
limY = (len(lines[0]))-1
antinodes = set()
for key in pos:
    if len(pos[key])>1:
        values = list(map (lambda x :  list(map(int,x.split(","))),pos[key]))
        for i in range(0,len(values)-1):
            first = values[i]
            for other in values[i+1:]:
                x = first[0]-other[0]
                y = first[1]-other[1]
                if 0<=first[0]+x<limX and 0<=first[1]+y<limY:
                    toStr = str(first[0]+x)+','+str(first[1]+y)
                    if not(toStr in antinodes):
                        antinodes.add(toStr)
                if 0<=other[0]-x<limX and 0<=other[1]-y<limY:
                    toStr = str(other[0]-x)+','+str(other[1]-y)
                    if not(toStr in antinodes):
                        antinodes.add(toStr)
print(len(antinodes))
           
