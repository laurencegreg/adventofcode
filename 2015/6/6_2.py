import re
f = open("input")
lines = f.readlines()
f.close()


lights = [False]*1000
for i in range (0,1000):
    lights[i]=[0]*1000
for line in lines :
    coords = list(map(int,re.findall("\d+", line)))
    for x in range(coords[0],coords[2]+1) :
        for y in  range(coords[1],coords[3]+1) :
            if "on" in line :
                lights[x][y]+=1
            if "off" in line :
                lights[x][y]=0 if lights[x][y]==0 else lights[x][y]-1
            if "toggle" in line :
                lights[x][y]+=2


print(sum(list(map(sum,lights))))



