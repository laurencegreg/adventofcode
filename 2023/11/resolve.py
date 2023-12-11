from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

input = []

for line in lines : 
    input.append(list(line.strip('\n')))


j = 0
while j < len(input[0]):
    if not '#' in list(map(lambda l: l[j],input)):
        for l in input :
            l.insert(j,'.')

        j+=1
    j+=1

expand = []
for i in range(0,len(input)):
    expand.append(input[i])
    if not '#' in input[i]:
        expand.append(input[i])

galaxies = []
for i in range(0,len(expand)):
    for j in range(0,len(expand[i])):
        if expand[i][j]=='#':
            galaxies.append([i,j])
            
dist = 0
for i in range(0,len(galaxies)-1):
    pos = galaxies[i]
    dist += sum(
                list(
                    map(
                        (lambda x:(abs(x[0]-pos[0])+abs(x[1]-pos[1])))
                        ,galaxies[i+1:]
                    )
                )
            )

print(dist)