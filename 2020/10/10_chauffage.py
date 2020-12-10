import re

f = open("input")
lines = f.readlines()
f.close()
lines = list(map(int, lines))
lines.sort()
lines.insert(0,0)
end = str(lines[len(lines)-1]+3)
counter = 0

def daway (pos,path):
    if pos == len(lines)-1 :
        global counter
        counter+=1
        print(path+", ("+end+")")
    else :
        for i in range(pos+1,min(len(lines),pos+4)):
            val = lines[pos]
            if lines[i]<val+4 :
                daway(i,path+", "+str(lines[i]))

daway(0,"(0)")
    
print(counter)