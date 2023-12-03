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
    d = {}
    for set in split[1].split(';'):
        for cubes in set.split(','):
            cube = cubes.strip().split(' ')
            nb=int(cube[0])
            color=cube[1]
            if color in d :
                d[color]=d[color] if d[color]>nb else nb
            else :
                d[color]=nb
    power = 1
    for i in d.values() :
        power *= i
    res += power

print(res)