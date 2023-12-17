from collections import Counter
import re
f = open("input")
lines = f.readlines()
input = []
energy = []
dir ={'>':[0,1],'<':[0,-1],'^':[-1,0],'v':[1,0]}
move = {}
move['.']={'>':['>'],'v':['v'],'^':['^'],'<':['<']}
move['/']={'>':['^'],'v':['<'],'^':['>'],'<':['v']}
move['\\']={'>':['v'],'v':['>'],'^':['<'],'<':['^']}
move['\\']={'>':['v'],'v':['>'],'^':['<'],'<':['^']}
move['|']={'>':['^','v'],'v':['v'],'^':['^'],'<':['^','v']}
move['-']={'>':['>'],'v':['<','>'],'^':['<','>'],'<':['<']}

for line in lines :
    input.append(list(line.strip('\n')))
    energy.append(list(map(lambda x:[] ,list(line.strip('\n')))))

class Beam:
    def __init__(self,pos,dest):
        self.pos = pos
        self.dest = dest

    def step(self):
        res = []
        for newDest in move[input[self.pos[0]][self.pos[1]]][self.dest]:
            e = dir[newDest]
            next = [self.pos[0]+e[0],self.pos[1]+e[1]]
            if (0<=next[0]<len(input)) and (0<=next[1]<len(input[0])):
                if not newDest in energy[next[0]][next[1]]:
                    energy[next[0]][next[1]].append(newDest)
                    res.append(Beam(next,newDest))                   
        return res
    
    def __str__(self):
        return str(self.pos)+" "+self.dest

beams = [Beam([0,0],'>')]
energy[0][0].append('>')
# print('--------------------------')
# for e in exps:
#     print(e)
while len(beams)!=0:
    tmp = []
    for beam in beams:
        tmp.extend(beam.step())
    beams=tmp
    # print('--------------------------')
    # for e in exps:
    #     print(e)
fin = 0
for e in energy :
    fin+= sum(list(map(lambda x:1 if len(x)>0 else 0,e)))

print(fin)