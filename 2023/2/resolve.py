import re
f = open("input")
lines = f.readlines()
f.close()

max = {}
max['red']=12
max['green']=13
max['blue']=14

res = 0

for line in lines :
    split = line.strip('\n').split(':')
    game = split[0].split(' ')[1]
    error = False
    for set in split[1].split(';'):
        d = {}
        for cubes in set.split(','):
            cube = cubes.strip().split(' ')
            d[cube[1]]=int(cube[0])
        for color in d :
            error = error or (d[color]>max[color])
    if (not error):
        res += int(game)

print(res)