import re
import itertools

f = open("input")
lines = f.readlines()
f.close()
time = 1

maximum = 0
for line in lines :
    values = list(map(int,(list(re.findall("\d+",line)))))
    allTime = values[1]+values[2]
    distance = (time//allTime*values[1]+min(values[1],time%allTime))*values[0]
    maximum = max(maximum,distance)
    print(line.split(" ")[0],distance)
print(maximum)