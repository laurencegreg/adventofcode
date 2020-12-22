import re
f = open("input")
lines = f.readlines()
f.close()

dicoRules = {}
dicoFinals = {}
it = 0
while ':' in lines[it] :
    lineSplit = lines[it].split(":")
    rules = lineSplit[1].strip('\n')
    name = lineSplit[0].strip()
    print(name,rules)
    if "a" in rules :
        dicoFinals[name]=set("a")
    elif "b" in rules :
        dicoFinals[name]=set("b")
    elif "|" in rules :
        dicoRules[name] = []
        for rule in rules.split("|"):
            dicoRules[name].append(rule.strip().split(" "))
    else :
        dicoRules[name]=[rules.strip().split(" ")]
    it+=1

subStates = list(dicoRules.keys())

while not set(["42","31"]).issubset(dicoFinals.keys())  :
    for name in  subStates :
        if sum(list(map(lambda l : set(l).issubset(dicoFinals.keys()),dicoRules[name]))) == len(dicoRules[name]) :
            print("compute for state "+name)
            finalRules = set("")
            #name -> states | states
            for states in dicoRules[name] :
                step = set()
                step.add("")
                #name -> state state | ...
                for state in states :
                    stateFinals = dicoFinals[state]
                    tmp = set()
                    #state -> abba | abab |...
                    for f in stateFinals :
                        for s in step :
                            tmp.add(s+f)
                    step = tmp
                finalRules.update(step)
            dicoFinals[name]=finalRules

    subStates = list(set(dicoRules.keys()) - set(dicoFinals.keys()))



dico31 = dicoFinals["31"]
dico42 = dicoFinals["42"]
print(dico31)
#print(min(list(map(len,dico31))))
#print(max(list(map(len,dico31))))
print(dico42)
#print(min(list(map(len,dico42))))
#print(max(list(map(len,dico42))))
# 0 -> 42^x 42^y 31^y  x>0 y>0

n = max(list(map(len,dico42)))
print(n)

def trad (s) :
    if len(s)==8 :
        if s in dico31 :
            return "31"
        elif s in dico42 :
            return "42"
    return s

count = 0
for line in lines[it+1:] :
    line = line.strip("\n")
    if len(line) % n == 0 and len(line) // n >= 3 :
        splitted = [line[i:i+n] for i in range(0, len(line), n)]
        print(splitted)
        statesList = list(map(trad,splitted))
        if statesList[0]=="42" and statesList[-1]=="31" and sum(list(map(lambda x : 1 if x == "42" else 0,statesList))) > sum(list(map(lambda x : 1 if x == "31" else 0,statesList))) :
            print(statesList)
            status = True
            state = statesList[0]
            for i in range(1,len(statesList)) :
                if statesList[i]!=state and statesList[i] == "42":
                    status = False
                state=statesList[i]
            if status :
                count+=1

print(count)