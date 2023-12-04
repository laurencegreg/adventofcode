import re
f = open("input")
lines = f.readlines()
f.close()


res = 0

for line in lines :
    split = line.strip('\n').split(': ')
    game = split[0].split(' ')[1]
    split = split[1].split(' | ')
    winning = set(filter(None,split[0].split(' ')))
    number = set(filter(None, split[1].split(' ')))
    tmp = (len(number & winning)-1)
    res += 2 ** tmp if tmp>=0 else 0

print(res)