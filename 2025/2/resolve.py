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
    if len(right)==len(left):
        if len(left)%2==0 :
            min = left[0:len(left)//2]
            max = right[0:len(right)//2]
            if (int(min+min)>= int(left)) and (int(min+min)<=int(right)):
                res +=int(min+min)
            if (min != max) and (int(max+max)<= int(right)):
                res +=int(max+max)
            for i in range(int(min)+1,int(max)):
                res += int(str(i)+str(i))
    else : 
        for l in range(len(left),len(right)+1):
            if l%2==0 : 
                min = '1'+('0'*(l//2-1))
                max = '9'*(l//2)
                if l == len(left):
                    min = left[0:l//2]
                elif l ==len(right):
                    max = right[0:l//2]
                if  (int(min+min)>= int(left)) and (int(min+min)<=int(right)):
                    res +=int(min+min)
                if  (min != max) and (int(max+max)<= int(right)):
                    res +=int(max+max)
                for i in range(int(min)+1,int(max)):
                    res += int(str(i)+str(i))
print(res)
