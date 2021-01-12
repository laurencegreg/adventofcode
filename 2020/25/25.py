import re
f = open("input")
lines = f.readlines()
f.close()

def step(value,subject):
    return (value*subject)%20201227

def findLoop(key):
    value = 1 
    steps = 0
    while value != key :
        value=step(value,7)
        steps+=1
    return steps

card = int(lines[0].strip("\n"))
cardSteps = findLoop(card)
door = int(lines[1].strip("\n"))

encryptKey = 1
for i in range(0,cardSteps):
    test = step(encryptKey,door)

print(encryptKey)
