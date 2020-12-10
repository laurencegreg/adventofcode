f = open("input")
lines = f.readlines()
f.close()

positions = set(["0-0"])

def delivering (list):
    x = 0
    y = 0
    for d in list :
        if d=='<' :
            x -= 1
        if d=='>' :
            x += 1
        if d=='^' :
            y += 1 
        if d=='v' :
            y -= 1
        positions.add(str(x)+"-"+str(y))

delivering(lines[0][0::2])
delivering(lines[0][1::2])
print(len(positions))