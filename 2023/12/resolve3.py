from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

# pour chaque entrée sans point ?### etc 
# avoir la liste des decoupages possibles associé à un booleen qui dit si le choix commence par un #
# exempe ?### -> [[3],false],[[4],true]
#poss ={'':[[[0],True]]}

# element exemple [[1,2],true]
# ajout d'un #
def addElt (elt):
    if elt[1]:
        return [[elt[0][0]+1]+elt[0][1:],True]
    else :
        return [[1]+elt[0],True]
# fonction pour remplir poss et retourner le resultat correspondant
def possibilities(str):
    if str=='':
        return [[[0],True]]
    else :
        posStr = possibilities(str[1:])
        res = list(map(addElt,posStr))
        if str[0]=='?':
            res += list(map(lambda x : [x[0],False] ,posStr))
        return res
        
def cleanPoss(str):
    return list(map(lambda x: list(filter(lambda y : y!=0,x[0])),possibilities(str)))

def arrangement(lp,cr):
    if len(lp)==0 : 
        if len(cr)==0:
            return 1
        else :
            return 0
    else :
        res = 0
        lpo = lp[0]
        for a in lpo :
            if len(cr)>=len(a):
                if cr[:len(a)]==a :
                    res += arrangement(lp[1:],cr[len(a):])
        return res

fin = 0
for line in lines : 
    sp = line.strip('\n').split(" ")
    if '.' in sp[0]:
        vals = list(map(int,sp[1].split(',')))

        input = [sp[0]+"?"+sp[0]+"?"+sp[0]+"?"+sp[0]+"?"+sp[0],vals+vals+vals+vals+vals]
        p = list(filter(None,input[0].split('.')))
        print(input)
        crit = input[1]
        po = list(map(cleanPoss,p))
        arrange = arrangement(po,crit)
        print(arrange)
        fin += arrange

print(fin)