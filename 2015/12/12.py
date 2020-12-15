import re
f = open("input")
lines = f.readlines()
f.close()
print("...........part1..........")
listInt=[]
for line in lines :
    listInt += list(map(int,re.findall("-?\d+", line)))
print(sum(listInt))

print("...........part2..........")
listJson=[]
for line in lines :
    listJson += re.findall("-?\d+|{|}|\[|\]|\"red\"", line)

def accol(i):
    localInt = []
    red = False
    arrayLevel = 0
    while listJson[i] != '}' :
        if listJson[i] == '{' :
            (i,l)=accol(i+1)
            localInt += l
        elif listJson[i].lstrip('-+').isdigit():
            localInt.append(int(listJson[i]))
        elif listJson[i] == '[' :
            arrayLevel +=1
        elif listJson[i] == ']' :
            arrayLevel -=1
        elif "red" in listJson[i] and arrayLevel == 0 :
            red = True
        i+=1
    if listJson[i] == '}' :
        if not red :
            return (i,localInt)
        else :
            return (i,[])
    else:
        print("dafuk")



(_,listInt)=accol(1)
print(sum(listInt))