f = open("input")
lines = f.readlines()
f.close()

positions = set(["0-0"])
x = 0
y = 0
for d in lines[0] :
    if d=='<' :
        x -= 1
    if d=='>' :
        x += 1
    if d=='^' :
        y += 1 
    if d=='v' :
        y -= 1
    positions.add(str(x)+"-"+str(y))

print(sorted(positions))
print(len(positions))