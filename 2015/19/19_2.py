
f = open("newInput")
lines = f.readlines()
f.close()

replacements = []
i=0
while lines[i]!= "\n" :
    replacements.append(lines[i].strip('\n').split("=>"))
    i+=1

molecule = lines[i+1].strip('\n')

print(molecule)


def transform(mol,replacement):
    if replacement[1] in mol:
        x = molecule.find(replacement[1])
        y = x + len(replacement[1])
        return(molecule[0:x]+replacement[0]+(molecule[y:] if y<len(molecule) else ""),1)
    else :
        return (mol,0)

count = 0
while molecule != "X" :
    for replacement in replacements :
        (molecule,x)=transform(molecule,replacement)
        count+=x
    print(molecule,count)
print(count)