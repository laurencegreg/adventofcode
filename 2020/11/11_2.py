import copy
f = open("input")
lines = f.readlines()
f.close()

places = list(map(lambda line: list(line.strip('\n')),lines))
x = 0
y = 0
def direct(x,y,xd,yd,char,places):
    xx = x+xd
    yy = y+yd
    find = False
    res = 0
    while not find and (yy in range(0,len(places))) and (xx in range(0,len(places[0]))):
        if places[yy][xx] in "L#":
            find = True
            res = 1 if places[yy][xx]==char else 0
        xx +=xd
        yy +=yd
    return res

def around (x,y,char,places):
    sum=0
    for yd in range(-1,2):
        for xd in range(-1,2):
            if not(xd==0 and yd==0) :
                sum +=direct(x,y,xd,yd,char,places)
    return sum

def step (places) :
    newPlaces = copy.deepcopy(places)
    for y in range(0,len(places)):
        for x in range(0,len(places[y])):
            if places[y][x] in "L#" :
                occupied =  around(x,y,'#',places)
            if places[y][x]=='L':
                if occupied==0:
                    newPlaces[y][x]='#'
            if places[y][x]=='#':
                if occupied>=5:
                    newPlaces[y][x]='L'
    return newPlaces



nextPlaces = step(places)
while nextPlaces != places :
    places = nextPlaces
    nextPlaces = step(places)

print(sum(list(map(lambda line: line.count('#'),places))))