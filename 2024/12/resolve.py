from collections import Counter
import re
f = open("input")
lines = list(map(lambda x : list(x.strip('\n')),f.readlines()))
farr = list(map(lambda x:x.copy(),lines))
for i in range(0,len(lines)):
    for j in range(0,len(lines[i])):
        fences = 0
        if i==0:
            fences+=1
        else :
            fences+=1 if lines[i-1][j]!=lines[i][j] else 0
        if i==len(lines)-1:
            fences+=1
        else :
            fences+=1 if lines[i+1][j]!=lines[i][j] else 0
        if j==0:
            fences+=1
        else :
            fences+=1 if lines[i][j-1]!=lines[i][j] else 0
        if j==len(lines[i])-1:
            fences+=1
        else :
            fences+=1 if lines[i][j+1]!=lines[i][j] else 0
        farr[i][j]=fences

pos = set()
res = 0

def toStr(i,j):
    return str(i)+","+str(j)

def run(i,j,c):
    
    if 0<=i<len(lines) and 0<=j<len(lines[i]) and (not toStr(i,j) in pos) and lines[i][j]==c :
        pos.add(toStr(i,j))
        down = run(i+1,j,c)
        left = run(i,j+1,c)
        up = run(i-1,j,c)
        right = run(i,j-1,c)
        return [1+down[0]+left[0]+up[0]+right[0],farr[i][j]+down[1]+left[1]+up[1]+right[1]]
    else :
        return [0,0]

for i in range(0,len(lines)):
    for j in range(0,len(lines[i])):
        if not toStr(i,j) in pos:
            r = run(i,j,lines[i][j])
            res += r[0]*r[1]

print(res)