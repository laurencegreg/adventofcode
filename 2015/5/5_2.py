import re
f = open("input")
lines = f.readlines()
f.close()

print(sum(list(map(lambda line : 1 if re.findall("(.{2}).*\\1", line) and re.findall("(.).\\1", line) else 0,lines))))