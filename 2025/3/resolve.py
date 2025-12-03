from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()
res = 0
for line in lines : 
    sp = list(line.strip('\n'))
    first = max(sp)
    iFirst = sp.index(first)
    if iFirst != len(sp)-1 : 
        second = max(sp[iFirst+1:len(sp)])
        print(first+second)
        res+=int(first+second)
    else : 
        second = first
        sp[iFirst]='0'
        first = max(sp)
        print(first+second)
        res+=int(first+second)

print(res)