f = open("input")
lines = f.readlines()
f.close()

def valid(lst,i) :
    find = False
    index = i-25
    while not find and index < i-1 :
        j=index+1
        while not find and j < i :
            find = int(lst[i])==(int(lst[index])+int(lst[j]))
            j+=1
        index+=1
    return find

error = False
index = 25
target = 0
while not error and index < len(lines) :
    error = not valid(lines,index)
    if error :
        target = int(lines[index])
    else : 
        index += 1

print("*********target*************")
print(target)
print("***********set*************")

find = False
index = 0
while not find and index < len(lines) :
    counter = 0
    i = index
    while counter < target :
        counter += int(lines[i])
        i+=1
    if counter == target :
        find=True
        miniCount=int(lines[index])
        min=int(lines[index])
        max=int(lines[index])
        print("*******result range**********")

        for j in range(index+1,i) :
            val = int(lines[j])
            miniCount += val
            min = val if val < min else min
            max = val if val > max else max
            print(j,lines[j],miniCount)

        print("************result***********")
        print(min,max,min + max)
        print("****************************")
    print(index,counter)
    index+=1
