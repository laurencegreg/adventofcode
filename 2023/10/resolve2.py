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
#possibles starts
if start[0]!=0:
    c = input[start[0]-1][start[1]]
    if c in dir and 'S' in dir[c]:
        pos.append([start[0]-1,start[1],'S',[str(start[0])+','+str(start[1]),str(start[0]-1)+','+str(start[1])]])
        m[start[0]-1][start[1]].append(1)
if start[1]!=0:
    c = input[start[0]][start[1]-1]
    if c in dir and 'E' in dir[c]:
        pos.append([start[0],start[1]-1,'E',[str(start[0])+','+str(start[1]),str(start[0])+','+str(start[1]-1)]])
        m[start[0]][start[1]-1].append(1)
if start[0]!=(len(m)-1):
    c = input[start[0]+1][start[1]]
    if c in dir and 'N' in dir[c]:
        pos.append([start[0]+1,start[1],'N',[str(start[0])+','+str(start[1]),str(start[0]+1)+','+str(start[1])]])
        m[start[0]+1][start[1]].append(1)
if start[1]!=(len(m[start[0]])-1):
    c = input[start[0]][start[1]+1]
    if c in dir and 'W' in dir[c]:
        pos.append([start[0],start[1]+1,'W',[str(start[0])+','+str(start[1]),str(start[0])+','+str(start[1]+1)]])
        m[start[0]][start[1]+1].append(1)


#replace start
input[start[0]][start[1]]='J'

i=2
lP = set()
while len(pos)>0:
    tmp = []
    for p in pos :
        pip = input[p[0]][p[1]]
        nextDir = dir[pip][p[2]] if ((pip in dir) and (p[2] in dir[pip])) else ""
        if nextDir != "":
            x = p[0]+move[nextDir][0]
            y = p[1]+move[nextDir][1]
            l = p[3]
            if (x in range(0,len(m))) and (y in range(0,len(m[x]))):
                m[x][y].append(i)
                l.append(str(x)+','+str(y))
                tmp.append([x,y,inv[nextDir],l])
    pos = []
    for t in tmp:
        if len(m[t[0]][t[1]])<2:
            pos.append(t)
        else :
            lP.update(t[3])
    i+=1


res = 0
for i in range(0,len(input)):
    j=0
    score=0
    while j <len(input[i]):
        toStr = str(i)+','+str(j)
        if toStr in lP:
            if input[i][j]=='|':
                score = (score+1)%2
            elif input[i][j]=='F':
                j+=1
                while input[i][j]=='-':
                    j+=1
                if input[i][j]=='J':
                    score = (score+1)%2
            elif input[i][j]=='L':
                j+=1
                while input[i][j]=='-':
                    j+=1
                if input[i][j]=='7':
                    score = (score+1)%2
        else :
            res+=score
        j+=1

print(res)