from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

plan=[]
slope={
    '>':[0,1],
    '<':[0,-1],
    'v':[1,0],
    '^':[-1,0]
}

ways = [[0,1,[]]]
endWays = []
for line in lines : 
    plan.append(list(line.strip('\n')))

while len(ways)!=0:
    tempWays = []
    for x,y,path in ways: 
        if x==len(plan)-1 and y==len(plan[x])-2:
            endWays.append(len(path))
        elif x<0 or x==len(plan) or y<0 or y==len(plan[x]) or plan[x][y]=='#' or str(x)+','+str(y) in path :
            None
        elif plan[x][y]!='.':
            sl = slope[plan[x][y]]
            tempWays.append([x+sl[0],y+sl[1],path +[str(x)+','+str(y)]])
        else :
            tmpPath = path +[str(x)+','+str(y)]
            tempWays.append([x+1,y,tmpPath])
            tempWays.append([x-1,y,tmpPath])
            tempWays.append([x,y-1,tmpPath])
            tempWays.append([x,y+1,tmpPath])
    ways=tempWays

print(max(endWays))