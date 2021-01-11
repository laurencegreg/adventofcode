import re
f = open("input")
lines = f.readlines()
f.close()

#  /\/\
#  [][]
# /\∕\∕\
# [][][]
# \/\/\/
#  [][]
#  \/\/

#      
#    -1,1   1,1
# -2 0   0,0   2,0
#   -1,-1  1,-1
#     

dicoDirNum = {"se":"1","sw":"2","ne":"3","nw":"4","e":"5","w":"6"}
dicoNum = {"1":(1,-1),"2":(-1,-1),"3":(1,1),"4":(-1,1),"5":(2,0),"6":(-2,0)}
setTiles = set()

def addPos (position,direction):
    (x,y)=position
    (a,b)=direction
    return (x+a,y+b)

for line in lines :
    s=line.strip("\n")
    for key in dicoDirNum.keys() :
        s = s.replace(key,dicoDirNum[key])
    (x,y)=(0,0)
    for n in s :
        (x,y)=addPos((x,y),dicoNum[n])
    if (x,y) in setTiles :
        setTiles.remove((x,y))
    else :
        setTiles.add((x,y))
def getNeighbourhood():
    neighbourhood = set()
    for tile in setTiles :
        neighbourhood.add(tile)
        for direction in dicoNum.values() :
            neighbourhood.add(addPos(tile,direction))
    return neighbourhood

def blackNeighbours(position):
    (x,y)=position
    neighbours = set(map(lambda x : addPos(position,x),dicoNum.values()))
    return len(list(setTiles&neighbours))

def isAlive(position):
    nbNeighbours = blackNeighbours(position)
    if position in setTiles :
        return nbNeighbours==1 or nbNeighbours==2
    else :
        return nbNeighbours==2

for i in range(0,100):
    tmp = [tile for tile in getNeighbourhood() if isAlive(tile)]
    setTiles = set(tmp)

print(len(setTiles))