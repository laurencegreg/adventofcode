import operator
f = open("input")
lines = f.readlines()
f.close()

waypoint = [1,10]
position = [0,0]
def move(char,it) :
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
    global waypoint
    right=angle
    if char == 'L':
        if angle==90 :
            right=270
        if angle==270 :
            right=90
    if right==90 :
        waypoint=[-waypoint[1],waypoint[0]]
    if right==180 :
        waypoint=[-waypoint[0],-waypoint[1]]
    if right==270 :
        waypoint=[waypoint[1],-waypoint[0]]


def step(line):
    print(line.strip('\n'))
    char = line[0:1]
    it = int(line.strip('\n')[1:])
    global waypoint
    global position
    if char in "LR" :
        turn(char,it)
    else :
        if char in "NSEW" :
            waypoint=list(
                map(
                    operator.add,
                    waypoint,
                    move(char,it)))
        else :
            position=list(
                map(
                    operator.add,
                    position,
                    list(
                        map(
                            lambda x : x * it,
                            waypoint
                        )
                    )
                )
            )
    print("waypoint",waypoint)
    print("position",position)
    
    
for line in lines :
    step(line)

print("--->"+str(abs(position[0])+abs(position[1])))

