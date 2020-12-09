f = open("input")
lines = f.readlines()
f.close()
counter = 0

lst = []
for line in lines :
    if line == '\n':
        lst.sort()
        print(lst)
        counter += len(lst)
        lst=[]
    else :
        for answers in line.strip('\n').split(" ") :
            for char in answers :
                lst.append(char) if char not in lst else lst

print(lst)
counter+=len(lst)

print(counter)