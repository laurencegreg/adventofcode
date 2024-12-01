from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

res = 0
fstCol = []
scdCol = []

for line in lines : 
    sp = line.strip('\n').split()

    fstCol.append(int(sp[0]))
    scdCol.append(int(sp[1]))

fstCol.sort()
scdCol.sort()

for i in range(0,len(fstCol)) :
    if fstCol[i]>scdCol[i] :
        res += (fstCol[i]-scdCol[i])
    else :
        res += (scdCol[i]-fstCol[i])

print(res)