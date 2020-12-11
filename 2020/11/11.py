import copy
f = open("input")
lines = f.readlines()
f.close()

places = list(map(lambda line: list(line.strip('\n')),lines))
x = 0
y = 0
def step (places) :
    newPlaces = copy.deepcopy(places)
    for y in range(0,len(places)):
        for x in range(0,len(places[y])):
            if places[y][x]=='L':
                if around(x,y,'#',places)==0:
                    newPlaces[y][x]='#'
            if places[y][x]=='#':
                if around(x,y,'#',places)>=4:
                    newPlaces[y][x]='L'
    return newPlaces

def around (x,y,char,places):
    return sum(list(map(lambda line : line[max(0,x-1):min(x+2,len(line))].count(char),places[max(0,y-1):min(y+2,len(places))])))+(-1 if places[y][x]==char else 0)


nextPlaces = step(places)
while nextPlaces != places :
    places = nextPlaces
    nextPlaces = step(places)

print(sum(list(map(lambda line: line.count('#'),places))))