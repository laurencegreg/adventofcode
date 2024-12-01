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

c = Counter(scdCol)

for i in fstCol :
    res+=(c[i]*i)

print(res)