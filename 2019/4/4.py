def isValid(password):
    same = False
    pos = 1
    value = password[0]
    while pos < len(password) and int(password[pos])>= int(value) :
        same = same or password[pos]==value
        value=password[pos]
        pos+=1
    return same and pos==len(password)

validPass = set()

for i in range(153517,630396):
    if isValid(str(i)):
        validPass.add(i)

print(len(validPass))