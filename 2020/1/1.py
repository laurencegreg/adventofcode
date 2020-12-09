f = open("input")
lines = f.readlines()
f.close()


for i in range(0,len(lines)-1):
    for j in range(i+1,len(lines)-1) :
        for k in range(j+1,len(lines)-1) :
            if int(lines[i])+int(lines[j])+int(lines[k]) == 2020 :
                print int(lines[i])*int(lines[j])*int(lines[k])


