from collections import Counter
import re
f = open("input")
line = list(map(int,f.readlines()[0].strip('\n')))
f.close()

revFiles = []
spaces = []

for i in range(0,len(line)):
    if i%2 == 0 :
        revFiles.insert(0,line[i])
    else:
        spaces.append(line[i])

finalPos = {}
leftSpaces = spaces.copy()
for i in range(0,len(revFiles)):
    ind = 0
    while(ind<len(revFiles)-i and leftSpaces[ind]<revFiles[i]) :
        ind +=1
    if ind<len(revFiles)-i :
        leftSpaces[ind]=leftSpaces[ind]-revFiles[i]
        index = ind*2+1
        if index in finalPos :
            finalPos[index].append([len(revFiles)-i-1,revFiles[i]])
        else :
            finalPos[index]=[[len(revFiles)-i-1,revFiles[i]]]
    else:
        tmp = len(revFiles)-i-1
        finalPos[tmp*2]=[[tmp,revFiles[i]]]
res = 0
inc = 0
for i in range(0,len(line)):
    j = inc
    inc += line[i]
    if i in finalPos:
        for p in finalPos[i]:
            xP = p[0]
            for y in range(0,p[1]):
                res += xP*j
                j+=1


print(res)

