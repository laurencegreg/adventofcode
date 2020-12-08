f = open("input")
lines = f.readlines()
f.close()

def fun1(acc,i,lines) :
    lines2 = list(lines)
    if i == len(lines) :
        return ["ok",acc]
    if "end" in lines[i] :
        return ["ko",0]
    if "nop" in lines[i] :
        jump = int(lines[i].split(" ")[1])
        lines2[i]="end"
        return choice(fun1(acc,i+1,lines2),fun2(acc,i+jump,lines2))
    if "jmp" in lines[i] :
        add = int(lines[i].split(" ")[1])
        lines2[i]="end"
        return choice(fun2(acc,i+1,lines2),fun1(acc,i+add,lines2))
    if "acc" in lines[i] :
        add = int(lines[i].split(" ")[1])
        lines2[i]="end"
        return fun1(acc+add,i+1,lines2)

def fun2(acc,i,lines) :
    lines2 = list(lines)
    if i == len(lines) :
        return ["ok",acc]
    if "end" in lines[i] :
        return ["ko",0]
    if "nop" in lines[i] :
        lines2[i]="end"
        return fun2(acc,i+1,lines2)
    if "acc" in lines[i] :
        add = int(lines[i].split(" ")[1])
        lines2[i]="end"
        return fun2(acc+add,i+1,lines2)
    if "jmp" in lines[i] :
        jump = int(lines[i].split(" ")[1])
        lines2[i]="end"
        return fun2(acc,i+jump,lines2)


def choice(list1,list2):
    if list1[0] == "ok" :
        return list1
    return list2

print(fun1(0,0,lines))

