from collections import Counter
import re
f = open("input")
line = f.readlines()[0].strip('\n')

f.close()


def free(i):
    return i%2==1
start = 0
stLen = int(line[start])
end = len(line)-1
endLen = int(line[end])
if free(end):
    end -= 1
    endLen = int(line[end])

res = 0
it = 0
while start < end : 
    while stLen != 0:
        res += it*(start//2)
        it+=1
        stLen-=1
    for i in range(0,int(line[start+1])):
        if endLen==0:
            end -=2
            endLen = int(line[end])
        res+= it*(end//2)
        endLen -=1
        it+=1
    start +=2
    stLen = int(line[start])

for j in range(0,min(stLen,endLen)):
    res+= it*(end//2)
    it+=1

print(res)

    
