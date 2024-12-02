from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

res = 0
for line in lines : 
    sp = list(map(int,line.strip('\n').split()))
    diff = []
    for i in range(0,len(sp)-1):
        diff.append(sp[i]-sp[i+1])
    safe = 1<=abs(diff[0])<=3
    for i in range(0,len(diff)-1):
        safe  = safe and ((diff[i] >0 and diff[i+1] >0) or (diff[i+1]<0 and diff[i] <0)) and 1<=abs(diff[i+1])<=3
    i = 0
    while not(safe) and i<len(sp):
        diff = []
        for j in range(0,len(sp)-1):
            if j!=i :
                if (j!=len(sp)-2 or i!=len(sp)-1):
                    diff.append(sp[j]-sp[(j+1 if j+1!=i else j+2)])
        safe = 1<=abs(diff[0])<=3
        for j in range(0,len(diff)-1):
            safe  = safe and ((diff[j] >0 and diff[j+1] >0) or (diff[j+1]<0 and diff[j] <0)) and 1<=abs(diff[j+1])<=3
        i+=1
    res+=1 if safe else 0

print(res)