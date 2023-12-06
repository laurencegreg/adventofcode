from operator import truediv
import re
f = open("input")
lines = f.readlines()
f.close()

time = int(lines[0].strip('\n').split(':')[1].replace(' ',''))
distance = int(lines[1].strip('\n').split(':')[1].replace(' ',''))

i=0
j=time
while ((time-i)*i)<=distance:
    i+=1
while ((time-j)*j)<=distance:
    j-=1

print(j-i+1)