from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

arr = []
for line in lines :
    arr.append(list(line.strip('\n')))

def find(word,x,y):
    res = 0
    if arr[x][y]==word[0]:
        res += findDir(word[1:],x+1,y+1,1,1)
        res += findDir(word[1:],x,y+1,0,1)
        res += findDir(word[1:],x-1,y+1,-1,1)
        res += findDir(word[1:],x-1,y,-1,0)
        res += findDir(word[1:],x-1,y-1,-1,-1)
        res += findDir(word[1:],x,y-1,0,-1)
        res += findDir(word[1:],x+1,y-1,1,-1)
        res += findDir(word[1:],x+1,y,1,0)
    return res

def findDir(word,x,y,xi,yi):
    if len(word)==0 :
        return 1
    elif 0<=x<len(arr) and 0<=y<len(arr[x]):
        return findDir(word[1:],x+xi,y+yi,xi,yi) if word[0]==arr[x][y] else 0
    else :
        return 0
    
finalRes = 0
for i in range(0,len(arr)):
    for j in range(0,len(arr[i])):
        finalRes += find("XMAS",i,j)

print(finalRes)