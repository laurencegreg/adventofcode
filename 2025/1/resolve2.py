from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

pos = 50
res = 0

for line in lines : 
    sp = line.strip('\n')
    res += int(sp[1:])//100
    if (sp[0]=='R'):
        if ((pos != 0) & ((pos + (int(sp[1:])%100)) >= 100)) : 
            res += 1
        pos = (pos + int(sp[1:]))%100
    else :
        if ((pos != 0) & ((pos - (int(sp[1:])%100)) <= 0)) : 
            res += 1
        pos = (pos - int(sp[1:]))%100


print(res)