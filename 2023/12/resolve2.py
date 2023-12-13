from collections import Counter
import re
f = open("input.test")
lines = f.readlines()
f.close()

fin = 0
for line in lines : 
    sp = line.strip('\n').split(" ")
    vals = list(map(int,sp[1].split(',')))

    input = sp[0]+"?"+sp[0]+"?"+sp[0]+"?"+sp[0]+"?"+sp[0]
    vals = vals+vals+vals+vals+vals
    p = list(filter(None,input.split('.')))
    le = list(map(len,p))
    print(vals)
    print(sum(vals))
    print(le)
    print(sum(le))
    print(p)

print(fin)