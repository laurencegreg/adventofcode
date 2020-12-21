import re
f = open("input")
lines = f.readlines()
f.close()



def calc (subline) :
    pos = subline.find("+")
    simplified = subline
    while pos != -1 : 
        before = pos-1
        while before >=0 and simplified[before].isdigit() :
            before -=1
        before+=1
        after = pos+1
        while after < len(simplified) and simplified[after].isdigit() :
            after+=1
        simplified = simplified[0:before]+str(int(simplified[before:pos])+int(simplified[pos+1:after]))+("" if after >= len(simplified) else simplified[after:])
        pos = simplified.find("+")
    return eval(simplified)

count=0
for line in lines :
    step = line.replace(" ","").strip("\n")
    print(step)
    subcalc = re.search("\([^\(\)]*\)",step)
    while subcalc :
        step = step[0:subcalc.start()]+str(calc(subcalc.group(0)))+step[subcalc.end():]
        print(step)
        subcalc = re.search("\([^\(\)]*\)",step)
    count+=calc(step)

print(count)
