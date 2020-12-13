import re
f = open("input")
lines = f.readlines()
f.close()

splitted = lines[1].strip("\n").split(",")
busList = []
for i in range (0,len(splitted)):
    if splitted[i].isdigit() :
        busList.append([int(splitted[i]),i])

print(busList)

timestamp = 0
step = 1 
dicoFound = {}
maxFound=0
find = False
while not find :
    i = 0
    found = True
    while found and i<len(busList) :
        found = ((timestamp+busList[i][1])%busList[i][0])==0
        if found :
            if i>maxFound :
                print(timestamp,busList[i])
                if i in dicoFound.keys() :
                    step=timestamp-dicoFound[i]
                    maxFound = i 
                else:
                    dicoFound[i]=timestamp
            i+=1
    if i == len(busList) :
        find = True
    else :
        timestamp+=step

print(timestamp)
