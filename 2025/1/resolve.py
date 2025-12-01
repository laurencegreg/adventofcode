from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

pos = 50
res = 0

for line in lines : 
    sp = line.strip('\n')
    if (sp[0]=='R'):
        pos = (pos + int(sp[1:]))%100
    else :
        pos = (pos - int(sp[1:]))%100
    if pos == 0 :
        res += 1


print(res)