import re
f = open("input")
lines = f.readlines()
f.close()

maxId = 0

for line in lines :
    seatId = int(line.replace("F","0").replace("B","1").replace("L","0").replace("R","1"),2)
    print(seatId)
    if seatId > maxId :
        maxId = seatId

print(maxId)