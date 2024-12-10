from collections import Counter
import re
f = open("input")

lines = f.readlines()
f.close()

arr = []
for line in lines:
    arr.append(list(map(int,line.strip('\n'))))


trail = {}
def move(i,x,y,start):
    if 0<=x<len(arr) and 0<=y<len(arr[x]) and i==arr[x][y]:
        if i==9 :
            toStr = str(x)+','+str(y)
            if start in trail:
                trail[start].add(toStr)
            else :
                trail[start]={toStr}
            return 1
        else :
            return move(i+1,x+1,y,start)+move(i+1,x-1,y,start)+move(i+1,x,y+1,start)+move(i+1,x,y-1,start)
    else :
        return 0

res2=0
for x in range(0,len(arr)):
    for y in range(0,len(arr[x])):
        res2 +=move(0,x,y,str(x)+','+str(y))

res = 0
for st in trail:
    res += len(trail[st])

print(res)
print(res2)