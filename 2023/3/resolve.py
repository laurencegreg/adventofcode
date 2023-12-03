import re

f = open("input")
lines = f.readlines()
f.close()

ar = []
for line in lines :
    ar.append([char for char in line.strip('\n')])

symbols = []
for line in ar : 
    symbols.append(map((lambda x: True if ((x!='.') and (not unicode(x, 'utf-8').isnumeric())) else False),line))


def checkNeighbour(x,y):
    res = False
    for i in range((0 if x==0 else x-1),(x+1 if x+1 == len(symbols) else x+2)):
        for j in range((0 if y==0 else y-1),(y+1 if y+1 == len(symbols[i]) else y+2)):
            res = res or symbols[i][j]
    return res

sum = 0
for idx,line in enumerate(ar):
    i = 0
    while i < len(ar) :
        if unicode(line[i], 'utf-8').isnumeric():
            num = line[i]
            neighbour = checkNeighbour(idx,i)
            i+=1
            while (i < len(ar) and unicode(line[i], 'utf-8').isnumeric()) :
                if (not neighbour):
                    neighbour = checkNeighbour(idx,i)
                num += line[i]
                i+=1
            if neighbour : 
                sum += int(num)
        else :
            i+=1

print(sum)