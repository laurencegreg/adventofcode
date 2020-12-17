f = open("input")
lines = f.readlines()
f.close()

nums = list(map(int,lines))

def addChoice(l,count):
    if count==150 :
        return 1
    elif count > 150 :
        return 0
    else :
        return sum([
            addChoice(
                l[i+1:],
                count+l[i]
            ) for i in range(0,len(l)-1)]
            +[
                1 if count+l[-1]==150 else 0
            ])

print(addChoice(nums,0))