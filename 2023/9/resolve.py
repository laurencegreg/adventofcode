from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

res = 0
for line in lines : 
    ar = []
    sp = list(map(int,line.strip('\n').split()))

    ar.append(sp)
    while sum(sp)!=0:
        tmp = []
        for i in range(0,len(sp)-1):
            tmp.append(sp[i+1]-sp[i])
        sp = tmp
        ar.append(sp)
    for i in range(len(ar)-2,-1,-1):
        ar[i].append(ar[i][len(ar[i])-1]+ar[i+1][len(ar[i+1])-1])
    res +=ar[0][len(ar[0])-1]

print(res)