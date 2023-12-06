from operator import truediv
import re
f = open("input")
lines = f.readlines()
f.close()

time = int(lines[0].strip('\n').split(':')[1].replace(' ',''))
distance = int(lines[1].strip('\n').split(':')[1].replace(' ',''))

count=0
for j in range(0,time):
    if ((time-j)*j)>distance:
        count+=1


print(count)