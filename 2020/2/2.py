f = open("input")
lines = f.readlines()
f.close()
counter = 0
for line in lines :
    infos = line.split(" ")
    ranges = infos[0].split("-")
    if (infos[2].count(infos[1].replace(":","")) in range(int(ranges[0]),int(ranges[1])+1)) :
        counter +=1


print(counter)

