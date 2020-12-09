f = open("input")
lines = f.readlines()
f.close()
acc = 0
i=0
while "end" not in lines[i] :
    if "nop" in lines[i] :
        lines[i]="end"
        i+=1
    if "acc" in lines[i] :
        acc += int(lines[i].split(" ")[1])
        lines[i]="end"
        i+=1
    if "jmp" in lines[i] :
        jump = int(lines[i].split(" ")[1])
        lines[i]="end"
        i+=jump
print(acc)

