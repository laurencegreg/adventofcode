from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

ar = []
arBin = []
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

for line in lines : 
    sp = list(line.strip('\n'))
    if len(sp)>0:
        ar.append(list(map(lambda x: 1 if x=='#' else 0,sp)))
    else :
        arBin.append([list(map(binary,ar)),list(map(binary,(rev(ar))))])
        ar = []

arBin.append([list(map(binary,ar)),list(map(binary,(rev(ar))))])

def mirror(tab):
    res = 0
    it = 1
    while it<len(tab) and res==0:
        size = min(it,len(tab)-it)
        tmp = tab[it:it+size]
        tmp.reverse()
        if tab[it-size:it]==tmp:
            res=it
        it+=1
    return res

res = 0
for a in arBin:
    res += mirror(a[0])*100 + mirror(a[1])

print(res)