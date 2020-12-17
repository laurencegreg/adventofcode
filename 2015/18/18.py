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
            if places[y][x]=='#':
                if not around(x,y,'#',places) in range(2,4):
                    newPlaces[y][x]='.'
            if places[y][x]=='.':
                if around(x,y,'#',places)==3:
                    newPlaces[y][x]='#'
    return newPlaces

def around (x,y,char,places):
    return sum(list(map(lambda line : line[max(0,x-1):min(x+2,len(line))].count(char),places[max(0,y-1):min(y+2,len(places))])))+(-1 if places[y][x]==char else 0)

#part1

# for i in range(0,100):
#     places = step(places)

# print(sum(list(map(lambda line: line.count('#'),places))))

for i in range(0,100):
    places[0][0]='#'
    places[0][-1]='#'
    places[-1][0]='#'
    places[-1][-1]='#'
    places = step(places)

places[0][0]='#'
places[0][-1]='#'
places[-1][0]='#'
places[-1][-1]='#'

print(sum(list(map(lambda line: line.count('#'),places))))