from collections import Counter
import re
f = open("input.test")
lines = f.readlines()
f.close()

symbol = {}

symbol["N"]={"E":"F","N":"|","S":"^","W":"7"} 
symbol["S"]={"E":"L","N":"U","S":"|","W":"J"} 
symbol["E"]={"E":"-","N":"J","S":"7","W":">"} 
symbol["W"]={"E":"<","N":"L","S":"F","W":"-"} 

move = {}

move["N"]=[-1,0]
move["S"]=[1,0]
move["E"]=[0,1]
move["W"]=[0,-1]

cor = {}
cor["D"]="S"
cor["U"]="N"
cor["L"]="W"
cor["R"]="E"

plan = []
indPlan = 0
plan.append([['F'],0])

def addPlan(a,b,s,indPlan):
    index=indPlan
    if a in range(indPlan,indPlan+len(plan)):
        realX = a-indPlan
    else :
        if a<indPlan:
            for i in range(0,indPlan-a):
                plan.insert(0,[])
            index = a
            realX = 0
        else :
            #a>indPlan + len
            for i in range(indPlan+len(plan),a+1):
                plan.append([])
            realX = len(plan)-1
    
    linePlan = plan[realX]
    if len(linePlan)==0:
        linePlan.append([s])
        linePlan.append(b)
    else :
        if b < linePlan[1]:
            for j in range(0,linePlan[1]-b-1):
                linePlan[0].insert(0,'.')
            linePlan[0].insert(0,s)
            linePlan[1]=b
        elif b > linePlan[1]+len(linePlan[0])-1:
            for j in range(linePlan[1]+len(linePlan[0]),b):
                linePlan[0].append('.')
            linePlan[0].append(s)
        else :
            linePlan[0][b-linePlan[1]]=s
    return index
        


            

x = 0
y = 0
last = ''
for line in lines : 
    sp = line.split(' ')
    dir = cor[sp[0]]
    l = int(sp[1])
    if last=='':
        x += move[dir][0]
        y += move[dir][1]
        last = dir
        l -= 1
    while l != 0 :
        l-=1
        indPlan = addPlan(x,y,symbol[last][dir],indPlan)
        x += move[dir][0]
        y += move[dir][1]
        last = dir

for p in plan:
    print(p)
res = 0
for line in plan:
    lp = line[0]
    j=0
    score=0
    while j <len(lp):
        if lp[j] != '.':
            if lp[j]=='|':
                res+=1
                score = (score+1)%2
            elif lp[j]=='F':
                res+=1
                j+=1
                while lp[j]=='-':
                    res+=1
                    j+=1
                if lp[j]=='J':
                    res+=1
                    score = (score+1)%2
                else :
                    res+=1
            elif lp[j]=='L':
                res+=1
                j+=1
                while lp[j]=='-':
                    j+=1
                    res+=1
                if lp[j]=='7':
                    res+=1
                    score = (score+1)%2
                else :
                    res+=1
        else :
            res+=score
        j+=1
    print(res)
print(res)