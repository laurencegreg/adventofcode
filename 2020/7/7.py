import re

f = open("input")
lines = f.readlines()
f.close()

bagsSet = {}
for line in lines :
    bagName = ""
    bagContains = {}
    for bag in re.split("bags?",line) :  
        if not bagName :
            bagName = bag.strip().replace(" ","_")
        else :
            if '.' not in bag and "other" not in bag :
                bag ='_'.join(filter(lambda x: x.lower() not in ["contain",","], bag.split()))
                bagContains[bag[bag.find('_')+1:]]=int(bag[0:bag.find('_')])
    bagsSet[bagName]=bagContains

def hasShinyGold (bagName,bagPath) :
    if bagName == "shiny_gold" : 
        #print(bagPath)
        return True
    else:
        find = False
        for bag in bagsSet[bagName].keys() :
            find = find or hasShinyGold(bag,bagPath+"/"+bag)
        return find

counter = 0
for bag in bagsSet.keys() :
    if hasShinyGold(bag,bag) :
        counter+=1

print(counter-1)

def countBags (bagName) :
    numBags = 1
    for bag in bagsSet[bagName].keys() :
        numBags +=bagsSet[bagName][bag]*countBags(bag)
        
    return numBags

print(countBags("shiny_gold")-1)


