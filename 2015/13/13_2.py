import re
import itertools

f = open("input")
lines = f.readlines()
f.close()

likeness = {}

for line in lines :
    like = int(list(re.findall("\d+",line))[0])
    if "lose" in line :
       like = -1*like
    splitted = line.split(" ")
    name = splitted[0]
    neighbour = splitted[-1].strip(".\n")

    if not name in likeness.keys() :
       likeness[name]={}
    likeness[name][neighbour]=like

names = list(likeness.keys())

likeness["me"]={}
for name in names :
    likeness["me"][name]=0
    likeness[name]["me"]=0

names = list(likeness.keys())

maxChange = 0
for perm in list(itertools.permutations(names)):
    change = 0
    
    for i in range(0,len(perm)) :
        change += likeness[perm[i]][perm[i-1]] + likeness[perm[i]][perm[(i+1)%len(perm)]]
    maxChange = max(maxChange,change)

print(maxChange)