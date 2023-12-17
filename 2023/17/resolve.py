from collections import Counter
import re
f = open("input")
lines = f.readlines()
input = []
mini = []
dir ={'>':[0,1],'<':[0,-1],'^':[-1,0],'v':[1,0]}
move = {'>':['>','v','^'],'<':['<','v','^'],'^':['>','<','^'],'v':['>','v','<']}
for line in lines :
    input.append(list(map(int,list(line.strip('\n')))))
    mini.append(list(map(lambda x: {},list(line.strip('\n')))))
mini[0][0]['']=input[0][0]

class Explorer:
    def __init__(self,pos, last, score):
        self.pos = pos
        self.last = last
        self.score = score

    def step(self):
        res = []
        for dest in move[self.last[0]]:
            la = self.last
            sc = self.score
            if dest==self.last[0]:
                la +=dest
            else :
                la = dest
            if len(la)<=3:
                e = dir[dest]
                next = [self.pos[0]+e[0],self.pos[1]+e[1]]
                if (0<=next[0]<len(input)) and (0<=next[1]<len(input[0])):
                    sc+=input[next[0]][next[1]]
                    if (not la in mini[next[0]][next[1]]) or mini[next[0]][next[1]][la]>sc:
                        mini[next[0]][next[1]][la]=sc
                        res.append(Explorer(next,la,sc))                   
        return res
    
    def __str__(self):
        return str(self.pos)+" "+self.last+" "+str(self.score)

exps = [Explorer([1,0],'v',input[1][0]),Explorer([0,1],'>',input[0][1])]
# print('--------------------------')
# for e in exps:
#     print(e)
while len(exps)!=0:
    tmp = []
    for exp in exps:
        tmp.extend(exp.step())
    exps=tmp
    # print('--------------------------')
    # for e in exps:
    #     print(e)

print(min(mini[len(mini)-1][len(mini[0])-1].values()))