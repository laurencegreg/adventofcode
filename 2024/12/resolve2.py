from collections import Counter
import re
f = open("input")
lines = list(map(lambda x : list(x.strip('\n')),f.readlines()))
farr = list(map(lambda x:x.copy(),lines))

#border return fences position in x or y
def borders (i,j):
    value = []
    if i==0:
        value.append(["xup:"+str(i),j])
    else :
        if lines[i-1][j]!=lines[i][j]:
           value.append(["xup:"+str(i),j])
    if i==len(lines)-1:
        value.append(["xdn:"+str(i+1),j])
    else :
        if lines[i+1][j]!=lines[i][j]:
            value.append(["xdn:"+str(i+1),j])
    if j==0:
        value.append(["yup:"+str(j),i])
    else :
        if lines[i][j-1]!=lines[i][j]:
            value.append(["yup:"+str(j),i])
    if j==len(lines[i])-1:
        value.append(["ydn:"+str(j+1),i])
    else :
        if lines[i][j+1]!=lines[i][j]:
            value.append(["ydn:"+str(j+1),i])
    return value

pos = set()
res = 0

def toStr(i,j):
    return str(i)+","+str(j)

def run(i,j,c,setBord):
    if 0<=i<len(lines) and 0<=j<len(lines[i]) and (not toStr(i,j) in pos) and lines[i][j]==c :
        arr = borders(i,j)
        for x in range(0,len(arr)):
            if arr[x][0] in setBord:
                setBord[arr[x][0]].add(arr[x][1])
            else :
                setBord[arr[x][0]]={arr[x][1]}
        pos.add(toStr(i,j))
        down = run(i+1,j,c,setBord)
        left = run(i,j+1,c,setBord)
        up = run(i-1,j,c,setBord)
        right = run(i,j-1,c,setBord)
        

        return 1+down+left+up+right
    else :
        return 0

for i in range(0,len(lines)):
    for j in range(0,len(lines[i])):
        if not toStr(i,j) in pos:
            sB = {}
            size = run(i,j,lines[i][j],sB)
            bord = 0
            for b in sB :
                bSorted = sorted(sB[b])
                x = -2
                for p in bSorted:
                    if p-x > 1:
                        bord+=1
                    x=p
            res+=size*bord



print(res)