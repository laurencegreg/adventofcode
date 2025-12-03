from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()
res = 0
for line in lines : 
    left = 0
    tmp = ""
    sp = list(line.strip('\n'))
    for i in range(12,0,-1):
        step = max(sp[left:len(sp)-i+1])
        left = sp[left:len(sp)-i+1].index(step)+left+1
        tmp +=step
    print(tmp)
    res+=int(tmp)

print(res)