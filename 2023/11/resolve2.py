from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

input = []

for line in lines : 
    input.append(list(line.strip('\n')))

expI = []
expJ = []
j = 0
while j < len(input[0]):
    if not '#' in list(map(lambda l: l[j],input)):
        expJ.append(j)
    j+=1

for i in range(0,len(input)):
    if not '#' in input[i]:
        expI.append(i)

galaxies = []
exp = 1000000-1
for i in range(0,len(input)):
    for j in range(0,len(input[i])):
        if input[i][j]=='#':
            galaxies.append([i+(len(list(filter(lambda x:x<i,expI)))*exp),j+(len(list(filter(lambda x:x<j,expJ))*exp))])


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