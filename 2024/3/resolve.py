from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

res = 0
for line in lines :
    pattern = "(mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\))"
    matches = re.findall(pattern, line)
    for m in matches:
        t = list(map(int,m[4:][:-1].split(",")))
        res += t[0]*t[1]
print(res)