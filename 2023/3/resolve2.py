import re

f = open("input")
lines = f.readlines()
f.close()

ar = []
for line in lines :
    ar.append([char for char in line.strip('\n')])

symbols = []
for line in ar : 
    symbols.append(map((lambda x: True if (x=='*') else False),line))


def checkNeighbour(x,y):
    res = set()
    for i in range((0 if x==0 else x-1),(x+1 if x+1 == len(symbols) else x+2)):
        for j in range((0 if y==0 else y-1),(y+1 if y+1 == len(symbols[i]) else y+2)):
            if(symbols[i][j]):
                res.add(str(i)+','+str(j))
    return res

gears = {}
for idx,line in enumerate(ar):
    i = 0
    while i < len(ar) :
        if unicode(line[i], 'utf-8').isnumeric():
            num = line[i]
            neighbours = checkNeighbour(idx,i)
            i+=1
            while (i < len(ar) and unicode(line[i], 'utf-8').isnumeric()) :
                neighbours = neighbours.union(checkNeighbour(idx,i))
                num += line[i]
                i+=1 
            for gear in neighbours :
                if gear in gears :
                    gears[gear].append(int(num))
                else :
                    gears[gear] = [int(num)]
        else :
            i+=1

num = 0
for gear in gears : 
    parts = gears[gear]
    if len(parts)==2 : 
        num += parts[0]*parts[1]

print(num)