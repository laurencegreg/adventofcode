from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

init = []
for line in lines :
    if line!='\n':
        init.append(list(line.strip('\n')))
length = len(init)
pivot = []
for i in range(0,len(init)):
    pivot.append(list(map(lambda x:x[i],init)))

for col in pivot :
    it = 0
    while it<len(col):
        if col[it]=='.':
            it2 = it+1
            while it2<len(col) and col[it2]=='.':
                it2+=1
            if it2<len(col) and col[it2]=='O':
                col[it]='O'
                col[it2]='.'
        it+=1

res = 0
def value(ide):
    i,x = ide
    return length-i if x=='O' else 0
for col in pivot:
    res += sum(list(map(value,enumerate(col))))
print(res)