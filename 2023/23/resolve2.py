from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

move={
    '<':[0,-1],
    '>':[0,1],
    '^':[-1,0],
    'v':[1,0]
}

rev={
    '<':'>',
    '>':'<',
    '^':'v',
    'v':'^'
}
plan=[]

for line in lines : 
    plan.append(list(re.sub('<|>|v|\^','.',line.strip('\n'))))

end = [len(plan)-1,len(plan[0])-2]
def part (ar,score):
    x = ar[0]
    y = ar[1]
    if x == end[0] and y == end[1]:
        return [[ar],score]
    dests = list(move.keys())
    dests.remove(rev[ar[2]])
    dest = []
    for d in dests :
        nx = x+move[d][0]
        ny = y+move[d][1]
        if nx>=0 and nx<len(plan) and ny>=0 and y<len(plan[nx]) and plan[nx][ny]!='#':
            dest.append([nx,ny,d])
    if len(dest)==0:
        return None
    elif len(dest)==1:
        return part(dest[0],score+1)
    else :
        return [dest,score+1]

resume={}
pos = [[0,1,'v']]
while len(pos)!= 0: 
    newPos = []
    for p in pos:
        res = part(p,0)
        if res != None :
            resume[','.join(list(map(str,p)))]=[list(map(lambda x: ','.join(list(map(str,x))),res[0])),res[1]]
            for d in res[0]:
                toS = (','.join(list(map(str,d))))
                if not toS in resume:
                    newPos.append(d)
    pos = newPos

def prev (st):
    sp = st.split(',')
    r = move[rev[sp[2]]]
    return str(int(sp[0])+r[0])+','+str(int(sp[1])+r[1])

paths = [[["0,0"],"0,1,v",0]]
res = 0
strEnd = str(end[0])+','+str(end[1])

while len(paths)!=0 :
    newPaths = []
    for p in paths:
        next = p[1]
        if next.startswith(strEnd):
            if res < p[2] :
                res = p[2]
        else :
            if next in resume :
                for n in resume[next][0]:
                    croisement = prev(n)
                    if not croisement in p[0]:
                        newPaths.append([p[0]+[croisement],n,p[2]+resume[next][1]])
    paths = newPaths
print(res)
