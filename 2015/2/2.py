f = open("input")
lines = f.readlines()
f.close()

def paper (line) :
    [l,w,h]=list(map(int,line.strip('\n').split("x")))
    sides=[l*w,w*h,h*l]
    return sum(list(map(lambda x : x*2,sides)))+min(sides)

print(sum(list(map(paper,lines))))