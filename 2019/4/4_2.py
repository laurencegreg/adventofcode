def isValid(password):
    same = False
    previousSame = 0
    pos = 1
    value = password[0]
    while pos < len(password) and int(password[pos])>= int(value) :
        if password[pos]==value :
            previousSame+=1
        else :
            same = same or previousSame==1
            previousSame=0
        value=password[pos]
        pos+=1
    return (same or previousSame==1) and pos==len(password)

validPass = set()

for i in range(153517,630396):
    if isValid(str(i)):
        validPass.add(i)

print(len(validPass))