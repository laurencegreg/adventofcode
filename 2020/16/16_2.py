import re

f = open("input")
lines = f.readlines()
f.close()

valids = set()
invalids = []
validTickets = []
fields ={}
i = 0
while lines[i] !="\n" :
    ranges = list(map(int,re.findall("\d+",lines[i])))
    fieldName = lines[i].split(":")[0]
    rangeSet = set()
    j=0
    while j<len(ranges) :
        valids |= set(range(ranges[j],ranges[j+1]+1))
        rangeSet |= set(range(ranges[j],ranges[j+1]+1))
        j+=2
    fields[fieldName]=rangeSet
    i+=1

i+=2
myNumbers =list(map(int,lines[i].strip("\n").split(",")))
i+=3
while i<len(lines):
    numbers = list(map(int,lines[i].strip("\n").split(",")))
    valid=True
    for num in numbers :
        if not num in valids :
            valid=False
    if valid :
        validTickets.append(numbers)
    i+=1

possibilities = {}
for it in range(0,len(myNumbers)) :
    names = set()
    for field in list(fields.keys()):
        if myNumbers[it] in fields[field] :
            names.add(field)
    possibilities[it]=names

for ticket in validTickets :
   for it in range(0,len(ticket)) :
        names = set()
        for field in list(fields.keys()):
            if ticket[it] in fields[field] :
                names.add(field)
        possibilities[it]&=names

finals = {}
while len(possibilities) != 0 :
    for it in list(possibilities.keys()):
        if len(possibilities[it])==1 :
            name = possibilities[it].pop()
            possibilities.pop(it)
            finals[it]=name
            for clean in list(possibilities.keys()):
                possibilities[clean].discard(name)

print(finals)

result = 1
for it in list(finals.keys()) :
    if "departure" in finals[it]:
        result*=myNumbers[it]

print(result)