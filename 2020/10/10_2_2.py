import re

f = open("input")
lines = f.readlines()
f.close()
lines = list(map(int, lines))
lines.sort()
lines.insert(0,0)
lines.append(lines[len(lines)-1]+3)

result=[1]
   
for i in range(1,len(lines)):
    possibilities = 0
    for j in range(max(0,i-3),i) :
        if lines[i]-lines[j]<=3 :
            possibilities += result[j]
    result.append(possibilities)

print(result[len(result)-1])