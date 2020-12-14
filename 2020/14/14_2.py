import re
f = open("input")
lines = f.readlines()
f.close()

mask="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
binArray=""
mem = {}
def applyMask(string,value,index) :
    if index==len(mask) :
        global mem
        print(int(string,2),value)
        mem[int(string,2)]=value
    elif mask[index] == 'X':
        applyMask(string+"0",value,index+1)
        applyMask(string+"1",value,index+1)
    elif mask[index] == '0':
        applyMask(string+binArray[index],value,index+1)
    elif mask[index] == '1':
        applyMask(string+"1",value,index+1)
    else :
        print("questufoula")

for line in lines :
    if "mask" in line :
        mask = line.split("=")[1].strip(" \n")
    else :
        values = re.findall("\d+", line)
        binArray = list(bin(int(values[0]))[2:].zfill(36))
        applyMask("",int(values[1]),0)

print(sum(mem.values()))