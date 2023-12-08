from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

lr = {"L":0,"R":1}
dest = list(lines[0].strip('\n'))
dir = {}

for line in lines[2:] : 
    dir[line[0:3]]=[line[7:10],line[12:15]]

it = 0
end = False
pos = "AAA"
while not end :
    pos = dir[pos][lr[dest[it%len(dest)]]]
    it+=1
    end = (pos == "ZZZ")

print(it)