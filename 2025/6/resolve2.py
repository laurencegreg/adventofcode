from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

lines = [list(line.strip('\n')) for line in lines]

operators = lines[len(lines)-1]
res = 0


i = len(operators)-1
operator = " "
while(i>0):
    numbers = []
    found=False
    while not(found):
        tmp = ""
        for j in range(len(lines)-1):
            tmp = tmp+lines[j][i]
        numbers.append(int(tmp))
        if operators[i]!=" ":
            found = True
            operator = operators[i]
        i-=1
    if operator == '+':
        calc = 0
        for n in numbers:
            calc += n
    else :
        calc = 1
        for n in numbers:
            calc *= n
    res+=calc
    i-=1


print(res)