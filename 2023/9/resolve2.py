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
        ar[i].insert(0,ar[i][0]-ar[i+1][0])
    res +=ar[0][0]

print(res)