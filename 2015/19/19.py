import re
f = open("input")
lines = f.readlines()
f.close()

replacements = []
i=0
while lines[i]!= "\n" :
    replacements.append(list(re.findall("\w+",lines[i])))
    i+=1

molecule = lines[i+1]

res = set()
for repl in replacements :  
    for match in re.finditer(repl[0], molecule):
        (x,y) = match.span()
        res.add(molecule[0:x]+repl[1]+(molecule[y:] if y<len(molecule) else ""))

print(len(res))