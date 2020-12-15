import re
f = open("input")
lines = f.readlines()
f.close()
counter = 0
for line in lines :
    line = line.strip('\n')
    counter+=2
    for i in range(0,len(line)):
        # "
        if line[i]=='"' :
            counter+= 1
        # \
        if line[i]=='\\' :
            counter+=1

print(counter)
