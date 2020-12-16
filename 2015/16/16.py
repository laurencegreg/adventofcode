import re


f = open("input")
lines = f.readlines()
f.close()

auntDict = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

for line in lines :
    isSue = True
    for key in list(auntDict.keys()):
        if key in line and not key+": "+str(auntDict[key]) in line :
            isSue = False
            break
    if isSue :
        print(line)