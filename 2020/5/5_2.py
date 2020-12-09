import re
f = open("input")
lines = f.readlines()
f.close()

maxId = 0

seatId = lambda line : int(line.replace("F","0").replace("B","1").replace("L","0").replace("R","1"),2)
linesId = list(map(seatId, lines))
linesId.sort()

for i in range(1,len(linesId)-1) :
    if linesId[i]!= linesId[i-1]+1 :
        print linesId[i]-1
        binary = '{0:b}'.format(linesId[i]-1)
        print(binary[0:7].replace("0","F").replace("1","B")+binary[7:].replace("0","L").replace("1","R"))