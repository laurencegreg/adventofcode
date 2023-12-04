import re
f = open("input")
lines = f.readlines()
f.close()

dict = {}
for line in lines :
    split = line.strip('\n').split(': ')
    game = int(filter(None,split[0].split(' '))[1])
    dict[game]=1
res = 0

for line in lines :
    split = line.strip('\n').split(': ')
    game = int(filter(None,split[0].split(' '))[1])
    split = split[1].split(' | ')
    winning = set(filter(None,split[0].split(' ')))
    number = set(filter(None, split[1].split(' ')))
    tmp = len(number & winning)
    nb = dict[game]
    for i in range(game+1,game+tmp+1):
        dict[i]+=nb

print(sum(dict.values()))