from operator import truediv
import re
f = open("input")
lines = f.readlines()
f.close()

times = map(int,filter(None,lines[0].strip('\n').split(':')[1].split(' ')))
distances = map(int,filter(None,lines[1].strip('\n').split(':')[1].split(' ')))

nbRuns = 1

for i in range(0,len(times)):
    time=times[i]
    distance=distances[i]
    count=0
    for j in range(0,time):
        if ((time-j)*j)>distance:
            count+=1
    nbRuns=nbRuns*count

print(nbRuns)