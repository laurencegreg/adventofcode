import re
f = open("input")
lines = f.readlines()
f.close()

print(sum(list(map(lambda line : 1 if re.findall("(.)\\1",line) and len(re.findall("[aeiou]",line))>2 and not re.findall("ab|cd|pq|xy",line) else 0,lines))))