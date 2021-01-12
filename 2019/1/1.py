import re
f = open("input")
lines = f.readlines()
f.close()

fuel = sum(list(map(lambda line: int(line.strip("\n"))//3-2,lines)))
print("fuel : ",fuel)

