from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

res = 0
do = True
for line in lines : 
    pattern = "mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)|do\(\)|don\'t\(\)"
    matches = re.findall(pattern, line)
    
    for m in matches :
        if "don" in m :
            do = False
        elif "do" in m :
            do = True
        elif do :
            t = list(map(int,m[4:][:-1].split(",")))
            res += t[0]*t[1]
print(res)