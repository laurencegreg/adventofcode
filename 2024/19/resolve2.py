from collections import Counter
import math
f = open("input")
lines = f.readlines()
f.close()

patterns = lines[0].strip("\n").split(", ")
notFound = set()
founds = {"":1}
def find(line):
    if line in founds:
        return founds[line]
    if line in notFound :
        return 0
    selected = [p for p in patterns if line.startswith(p)]
    if len(selected)==0:
        return 0
    else:
        found = 0
        i = 0
        while i < len(selected):
            tmp = find(line[len(selected[i]):])
            if not(tmp):
                notFound.add(line[len(selected[i]):])
            else:
                found +=founds[line[len(selected[i]):]]
            i+=1
        if found > 0:
            founds[line]=found
        return found
            


res = 0

for i in range(2,len(lines)):
    line = lines[i].strip('\n')
    res = res+find(line)
    i+=1
print(res)