f = open("input")
lines = f.readlines()
f.close()
counter = 0
first=True

lst = [] 
for line in lines :
    if line == '\n':
        lst.sort()
        print(lst)
        counter += len(lst)
        lst=[]
        first=True
    else :
        for answers in line.strip('\n').split(" ") :
            answerList = []
            for char in answers :
                answerList.append(char)
            if first :
                lst = answerList
                first = False
            else :
                lst = [x for x in lst if x in answerList]

print(lst)
counter+=len(lst)

print(counter)