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
test = 20
while len(subStates) != 0 :
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

    test -= 1

print(sum(list(map(lambda line : 1 if line.strip("\n") in dicoFinals["0"] else 0,lines[it+1:]))))







