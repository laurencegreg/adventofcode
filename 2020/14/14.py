import re
f = open("input")
lines = f.readlines()
f.close()

mask="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
mem = {}
def applyMask(i) :
    binArray = list(bin(i)[2:].zfill(36))
    for it in range(0,len(mask)):
        if mask[it] != 'X':
            binArray[it]=mask[it]
    binStr = ''.join(binArray)
    return int(binStr,2)

for line in lines :
    if "mask" in line :
        mask = line.split("=")[1].strip(" \n")
    else :
        values = re.findall("\d+", line)
        mem[int(values[0])]=applyMask(int(values[1]))

print(sum(mem.values()))