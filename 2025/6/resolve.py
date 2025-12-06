from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

lines = [line.strip('\n').split() for line in lines]

res = 0 
for i in range(len(lines[0])):
    if lines[len(lines)-1][i] == '+':
        tmp = 0
        for j in range(len(lines)-1):
            tmp += int(lines[j][i])
    else:
        tmp = 1
        for j in range(len(lines)-1):
            tmp *= int(lines[j][i])
    res +=tmp

print(res)