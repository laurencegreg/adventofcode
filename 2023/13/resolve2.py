from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()


def binary (tab):
    res = 0
    for i in range(0,len(tab)):
        res += tab[i]*(2**i)
    return res

def rev (tab):
    revTab = []
    for i in range(0,len(tab[0])):
        revTab.append(list(map(lambda x : x[i],tab)))
    return revTab


def mirror(tab):
    res = []
    it = 1
    while it<len(tab):
        size = min(it,len(tab)-it)
        tmp = tab[it:it+size]
        tmp.reverse()
        if tab[it-size:it]==tmp:
            res.append(it)
        it+=1
    return res

arBin = []
init = []
res = 0
for line in lines :
    if line!='\n':
        init.append(line.strip('\n'))
    else:
        initBool = list(map(lambda x: list(map(lambda y: 1 if y=='#' else 0,list(x))),init))
        old = [mirror(list(map(binary,initBool))),mirror(list(map(binary,(rev(initBool)))))]
        found = False
        for i in range(0,len(init)):
            for j in range(0,len(init[i])):
                initBis = list(map(lambda x: list(map(lambda y: 1 if y=='#' else 0,list(x))),init))
                initBis[i][j]= (initBis[i][j]+1)%2
                tmp = [mirror(list(map(binary,initBis))),mirror(list(map(binary,(rev(initBis)))))]
                if (not found) and (tmp != old) and (tmp != [[],[]]):
                    for left in tmp[0]:
                        if not(left in old[0]):
                            res+=(left*100)
                    for right in tmp[1]:
                        if not(right in old[1]):
                            res+=right
                    found = True
        init = []



print(res)