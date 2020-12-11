import re
f = open("input")
lines = f.readlines()
f.close()


lights = [False]*1000
for i in range (0,1000):
    lights[i]=[False]*1000
for line in lines :
    coords = list(map(int,re.findall("\d+", line)))
    for x in range(coords[0],coords[2]+1) :
        for y in  range(coords[1],coords[3]+1) :
            if "on" in line :
                lights[x][y]=True
            if "off" in line :
                lights[x][y]=False
            if "toggle" in line :
                lights[x][y]=not lights[x][y]


print(sum(list(map(lambda line : line.count(True),lights))))



