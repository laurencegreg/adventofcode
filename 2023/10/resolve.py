from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

dir = {}

dir["|"]={"N":"S","S":"N"} 
dir["-"]={"W":"E","E":"W"} 
dir["L"]={"N":"E","E":"N"} 
dir["J"]={"N":"W","W":"N"}
dir["7"]={"S":"W","W":"S"} 
dir["F"]={"S":"E","E":"S"}

move = {}

move["N"]=[-1,0]
move["S"]=[1,0]
move["E"]=[0,1]
move["W"]=[0,-1]

inv = {}
inv["N"]="S"
inv["S"]="N"
inv["E"]="W"
inv["W"]="E"

input = []

for line in lines : 
    input.append(list(line.strip('\n')))

m=[]
start = []
for i in range(0,len(input)):
    mLine = []
    for j in range(0,len(input[i])):
        if input[i][j]=='S':
            mLine.append([0])
            start=[i,j]
        else :
            mLine.append([])
    m.append(mLine)

# for line in input :
#     print(line)

pos = []
if start[0]!=0:
    c = input[start[0]-1][start[1]]
    if c in dir and 'S' in dir[c]:
        pos.append([start[0]-1,start[1],'S'])
        m[start[0]-1][start[1]].append(1)
if start[1]!=0:
    c = input[start[0]][start[1]-1]
    if c in dir and 'E' in dir[c]:
        pos.append([start[0],start[1]-1,'E'])
        m[start[0]][start[1]-1].append(1)
if start[0]!=(len(m)-1):
    c = input[start[0]+1][start[1]]
    if c in dir and 'N' in dir[c]:
        pos.append([start[0]+1,start[1],'N'])
        m[start[0]+1][start[1]].append(1)
if start[1]!=(len(m[start[0]])-1):
    c = input[start[0]][start[1]+1]
    if c in dir and 'W' in dir[c]:
        pos.append([start[0],start[1]+1,'W'])
        m[start[0]][start[1]+1].append(1)

i=2
while len(pos)>0:
    tmp = []
    for p in pos :
        pip = input[p[0]][p[1]]
        nextDir = dir[pip][p[2]] if ((pip in dir) and (p[2] in dir[pip])) else ""
        if nextDir != "":
            x = p[0]+move[nextDir][0]
            y = p[1]+move[nextDir][1]
            if (x in range(0,len(m))) and (y in range(0,len(m[x]))):
                m[x][y].append(i)
                tmp.append([x,y,inv[nextDir]])
    pos = []
    for t in tmp:
        if len(m[t[0]][t[1]])<2:
            pos.append(t)
        else :
            print(m[t[0]][t[1]])
    i+=1

