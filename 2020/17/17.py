f = open("input")
lines = f.readlines()
f.close()

lighted = set()

for i in range(0,len(lines)) :
    line = lines[i]
    for j in range(0,len(line)) :
        if line[j]=='#' :
            lighted.add((i,j,0))

def neighbors(pos):
    (x,y,z)=pos
    res = set()
    for i in range(x-1,x+2) :
        for j in range(y-1,y+2) :
            for k in range(z-1,z+2) :
                if (i,j,k) != (x,y,z) :
                    res.add((i,j,k))
    return res

def lightedNeighbors(pos):
    return len(set.intersection(lighted,neighbors(pos)))

def step():
    neighborhood = set()
    for pos in list(lighted):
        neighborhood.add(pos)
        neighborhood.update(neighbors(pos))

    nextLighted = set()
    for pos in list(neighborhood):
        ln = lightedNeighbors(pos)
        if pos in lighted :
            if ln in [2,3] :
                nextLighted.add(pos)
        else :
            if ln == 3 :
                nextLighted.add(pos)
    return nextLighted

for i in range(0,6):
    lighted = step()

print(len(lighted))