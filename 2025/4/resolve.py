from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()
res = 0
tab = []
for line in lines : 
    tab.append(list(line.strip('\n')))

for i in range(0,len(tab)):
    for j in range(0,len(tab[i])):
        if tab[i][j] == '@':
            tmp = 0
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if x>=0 and x<len(tab) and y>=0 and y<len(tab[0]) and (x!=i or y!=j) and tab[x][y]!='.':
                        tmp +=1
            if tmp <4 :
                tab[i][j]='x'
                res+=1
print(res)