import re
f = open("input")
lines = f.readlines()
f.close()
counter = 0
for line in lines :
    line = line.strip('\n')
    i=0
    while i <len(line):
        # "
        if line[i]=='"' :
            counter+= 1
            i+=1
        # \x??
        elif line[i]=='\\' :
            if i+3<len(line) and line[i+1]=='x' :
                counter+=3
                i+=4
            else :
                if i+1<len(line) and line[i+1] in "nt" :
                    counter+=1
                counter+=1
                i+=2
        elif line[i]=='\n':
                counter+=1
                i+=1
        else :
            i+=1 
print(counter)
