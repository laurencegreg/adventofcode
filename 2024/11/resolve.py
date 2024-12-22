from collections import Counter
import re
f = open("input")
#part 1
step = 25
#part 2
#step = 75
line = f.readlines()
input = list(map(lambda x: [x,step],line[0].strip('\n').split(' ')))
f.close()

# input contient ['x',22] ou ['x',step,'fst,step-1'(,'scd,step-2' si il existe)]

resolved = {}

res = 0
def toStr (arr):
    return arr[0]+","+str(arr[1])

while len(input)>0 :
    current = input[0]
    input= input[1:]
    if len(current)>2:
        tmp = 0
        for i in range(2,len(current)):
            tmp +=resolved[current[i]]
        resolved[toStr(current[0:2])]=tmp
        if current[1]==step:
            res+=tmp
    else :
        st = toStr(current)
        if st in resolved :
            if current[1]==step:
                res+=tmp
        elif current[1]==0:
            resolved[st]=1
        else :
            if current[0]=='0':
                input.insert(0,[current[0],current[1],"1,"+str(current[1]-1)])
                input.insert(0,[str(1),current[1]-1])
            elif len(current[0])%2==0:
                fst = int(current[0][:len(current[0])//2])
                scd = int(current[0][len(current[0])//2:])
                input.insert(0,[current[0],current[1],str(fst)+","+str(current[1]-1),str(scd)+","+str(current[1]-1)])
                if not(str(fst)+","+str(current[1]-1) in resolved):
                    input.insert(0,[str(fst),current[1]-1])
                if not(str(scd)+","+str(current[1]-1) in resolved):
                    input.insert(0,[str(scd),current[1]-1])
            else :
                x = 2024*int(current[0])
                input.insert(0,[current[0],current[1],str(x)+","+str(current[1]-1)])
                if not(str(x)+","+str(current[1]-1) in resolved):
                     input.insert(0,[str(x),current[1]-1])
print(res)
