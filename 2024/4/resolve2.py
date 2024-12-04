from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

arr = []
for line in lines :
    arr.append(list(line.strip('\n')))

pos = {}
def findMAS(x,y):
    res = 0
    if arr[x][y]=='M':
        findAS(x+1,y+1,1,1)
        findAS(x-1,y+1,-1,1)
        findAS(x-1,y-1,-1,-1)
        findAS(x+1,y-1,1,-1)

def findAS(x,y,xi,yi):
    if 0<=x<len(arr) and 0<=y<len(arr[x]) and 0<=(x+xi)<len(arr) and 0<=(y+yi)<len(arr[(x+xi)]) :
        if  arr[x][y]=='A' and arr[x+xi][y+yi]=='S':
            key = str(x)+","+str(y)
            if key in pos :
                pos[key].append(str(xi)+","+str(yi))
            else :
                pos[key]=[str(xi)+","+str(yi)]
            
    
finalRes = 0
for i in range(0,len(arr)):
    for j in range(0,len(arr[i])):
        findMAS(i,j)

for key in pos :
    if len(pos[key])>1 :
        finalRes +=1 

print(finalRes)