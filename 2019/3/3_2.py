import re
f = open("input")
lines = f.readlines()
f.close()

dicoDir = {"R":(0,1),"L":(0,-1),"U":(1,0),"D":(-1,0)}

def addPosition(position,direction):
    (x,y)=position
    (a,b)=direction
    return (x+a,y+b)

snakeRoad = lines[0].strip("\n").split(",")
firstSnake = set()
dicoFirstSnake = {}
counter = 0
position = (0,0)
for moveDir in snakeRoad :
    direct = moveDir[0]
    length = int(moveDir[1:])
    for i in range(0,length) :
        counter+=1
        position = addPosition(position,dicoDir[direct])
        if not position in firstSnake :
            dicoFirstSnake[position]=counter
        firstSnake.add(position)

snakeRoad = lines[1].strip("\n").split(",")
secondSnake = set()
dicoSecondSnake = {}
counter=0
position = (0,0)
for moveDir in snakeRoad :
    direct = moveDir[0]
    length = int(moveDir[1:])
    for i in range(0,length) :
        counter+=1
        position = addPosition(position,dicoDir[direct])
        if not position in secondSnake :
            dicoSecondSnake[position]=counter
        secondSnake.add(position)

def posDistance(position):
    (x,y)=position
    return abs(x)+abs(y)

print(min(list(map(posDistance,list(map(lambda x: (dicoFirstSnake[x],dicoSecondSnake[x]),firstSnake & secondSnake))))))