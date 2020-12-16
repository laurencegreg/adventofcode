import re

f = open("input")
lines = f.readlines()
f.close()

valids = set()
invalids = []
i = 0
while lines[i] !="\n" :
    ranges = list(map(int,re.findall("\d+",lines[i])))
    j=0
    while j<len(ranges) :
        valids |= set(range(ranges[j],ranges[j+1]+1))
        j+=2
    i+=1

i+=5

while i<len(lines):
    numbers = list(map(int,lines[i].strip("\n").split(",")))
    for num in numbers :
        if not num in valids :
            invalids.append(num)
    i+=1

print(sum(invalids))