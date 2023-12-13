from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

input = []

def resolve(ar,count):
    if len(ar[1])==0:
        return 0 if '#' in ar[0] else 1
    if len(ar[0])==0:
        return 1 if (ar[1][0]==count and (len(ar[1])==1)) else 0
    if count==ar[1][0] :
        if (ar[0][0]=='?' or ar[0][0]=='.'):
            return resolve([ar[0][1:],ar[1][1:]],0)
        else:
            return 0
    else : 
        if count==0 :
            if ar[0][0]=='.':
                return resolve([ar[0][1:],ar[1]],0)
            elif ar[0][0]=='#':
                return resolve([ar[0][1:],ar[1]],1)
            else :
                return resolve([ar[0][1:],ar[1]],0)+resolve([ar[0][1:],ar[1]],1)
        else:
            if ar[0][0]=='#' or ar[0][0]=='?':
                return resolve([ar[0][1:],ar[1]],count+1)
            else :
                return 0
res = 0
for line in lines : 
    sp = line.strip('\n').split(" ")
    res +=resolve([list(sp[0]),list(map(int,sp[1].split(',')))],0)

print(res)



    