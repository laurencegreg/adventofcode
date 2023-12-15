from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()
fin = 0
init = lines[0].strip('\n').split(',')
for st in init :
    res = 0
    for c in st:
        res = (res+ord(c))*17%256
    fin+=res
print(fin)