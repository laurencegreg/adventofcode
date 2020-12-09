f = open("input")
lines = f.readlines()
f.close()
counter = 0
for line in lines :
    infos = line.split(" ")
    carac = infos[1][0]
    ranges = infos[0].split("-")
    if (infos[2][int(ranges[0])-1]==carac) != (infos[2][int(ranges[1])-1]==carac) :
        counter +=1


print(counter)

