from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()
res = 0
sp = lines[0].strip('\n').split(',')
for s in sp :
    tmp = s.split('-')
    left = tmp[0]
    right = tmp[1]
    tmpSet = set()
    for repeat in range (2,len(right)+1):
        if len(right)==len(left):
            if len(left)%repeat==0 :
                min = left[0:len(left)//repeat]
                max = right[0:len(right)//repeat]
                if (int(min*repeat)>= int(left)) and (int(min*repeat)<=int(right)):
                    tmpSet.add(int(min*repeat))
                if (min != max) and (int(max*repeat)<= int(right)):
                    tmpSet.add(int(max*repeat))
                for i in range(int(min)+1,int(max)):
                    tmpSet.add(int(str(i)*repeat))
        else : 
            for l in range(len(left),len(right)+1):
                if l%repeat==0 : 
                    min = '1'+('0'*(l//repeat-1))
                    max = '9'*(l//repeat)
                    if l == len(left):
                        min = left[0:l//repeat]
                    elif l ==len(right):
                        max = right[0:l//repeat]
                    if  (int(min*repeat)>= int(left)) and (int(min*repeat)<=int(right)):
                        tmpSet.add(int(min*repeat))
                    if  (min != max) and (int(max*repeat)<= int(right)):
                        tmpSet.add(int(max*repeat))
                    for i in range(int(min)+1,int(max)):
                        tmpSet.add(int(str(i)*repeat))
    res += sum(tmpSet)

print(res)

