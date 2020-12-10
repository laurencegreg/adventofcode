f = open("input")
lines = f.readlines()
f.close()

def paper (line) :
    lengths=list(map(int,line.strip('\n').split("x")))
    lengths.sort()
    return lengths[0]*2+lengths[1]*2+ lengths[0]*lengths[1]*lengths[2]

print(sum(list(map(paper,lines))))