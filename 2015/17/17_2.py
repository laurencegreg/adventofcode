f = open("input")
lines = f.readlines()
f.close()

nums = list(map(int,lines))

def addChoice(l,count,used):
    if count==150 :
        return [used]
    elif count > 150 :
        return None
    else :
        result = []
        for i in range(0,len(l)-1) :
            tmp = addChoice(l[i+1:],count+l[i],used+[l[i]])
            if not tmp == None :
                result+=tmp
        if count+l[-1]==150 :
            result.append(used+[l[-1]])
        return result if len(result) > 0 else None

possibilities = addChoice(nums,0,[])
minSize = min(list(map(len,possibilities)))
print(sum(list(map(
    lambda l : 1 if len(l)==minSize else 0,
    possibilities
))))
