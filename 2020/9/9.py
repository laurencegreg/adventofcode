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
            if find :
                print (lst[i],lst[index],lst[j])
            j+=1
        index+=1
    return find

error = False
index = 25
while not error and index < len(lines) :
    error = not valid(lines,index)
    if error :
        print(lines[index])
    else : 
        index += 1
