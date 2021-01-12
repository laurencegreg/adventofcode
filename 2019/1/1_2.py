import re
f = open("input")
lines = f.readlines()
f.close()

res = 0
for line in lines :
    fuel = int(line.strip("\n"))//3-2
    restFuel = fuel//3-2
    while restFuel > 0 :
        fuel+=restFuel
        restFuel = restFuel//3-2
    res+=fuel

print("real fuel : ",res )