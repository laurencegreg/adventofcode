import re

f = open("input")
lines = f.readlines()
f.close()
lines = list(map(int, lines))
lines.sort()
one = 0 if lines[0] == 3 else 1
three = 1 if lines[0] == 1 else 2

for i in range (1,len(lines)) :
    if (lines[i]-1)==lines[i-1] :
        one+=1
    else :
        three+=1
print(one)
print(three)
print(one*three)