import operator
f = open("input")
lines = f.readlines()
f.close()

dicDir = {0:[1,0],90:[0,1],180:[-1,0],270:[0,-1]}

direction = 90
position = [0,0]
def move(char,it) :
    go = list(map(lambda x : x*it,dicDir[direction]))
    if char=='N' :
        go = [it,0]
    if char=="S" :
        go = [-1*it,0]
    if char=="W" :
        go = [0,-1*it]
    if char=="E" :
        go = [0,it]
    return go

def turn(char,angle):
    global direction
    sign = -1 if char=='L' else 1
    direction = (direction+sign*angle)%360

def step(line):
    print(line.strip('\n'))
    char = line[0:1]
    it = int(line.strip('\n')[1:])
    global position
    if char in "LR" :
        turn(char,it)
    else :
        position=list(map(operator.add,position,move(char,it)))
    print(position)
    
    
for line in lines :
    step(line)

print("--->"+str(abs(position[0])+abs(position[1])))

