



def descent(right,down) :
    f = open("input")
    lines = f.readlines()
    f.close()
    downSteps = 1
    trees = 0
    pos = 0
    for line in lines :
        downSteps -= 1
        if downSteps == 0 :
            if (line[pos % (len(line)-1)] == '#') :
                trees +=1
            pos+=right
            downSteps=down

    return trees

print(descent(1,1),descent(3,1),descent(5,1),descent(7,1),descent(1,2))
print(descent(1,1)*descent(3,1)*descent(5,1)*descent(7,1)*descent(1,2))

