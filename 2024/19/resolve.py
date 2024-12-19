from collections import Counter
import math
f = open("input")
lines = f.readlines()
f.close()

patterns = lines[0].strip("\n").split(", ")
notFound = set()
def find(line):
    if len(line)==0:
        return True
    if line in notFound :
        return False
    selected = [p for p in patterns if line.startswith(p)]
    if len(selected)==0:
        return False
    else:
        found = False
        i = 0
        while not(found) and i < len(selected):
            tmp = find(line[len(selected[i]):])
            if not(tmp):
                notFound.add(line[len(selected[i]):])
            else:
                found = tmp
            i+=1
        return found
            


res = 0
for i in range(2,len(lines)):
    line = lines[i].strip('\n')
    res = res+1 if find(line) else res
    i+=1

print(res)