import re
f = open("input")
lines = f.readlines()
f.close()

correspondances = {}
matchs = {}

for line in lines :
    splitted = line.split(" ")
    ingredients = splitted[0:splitted.index("(contains")]
    allergens = list(map(lambda x : x.strip(")\n,"),splitted[splitted.index("(contains")+1:]))
    for allergen in allergens :
        if allergen in correspondances.keys() :
            correspondances[allergen] = correspondances[allergen] & set(ingredients)
        else :
            correspondances[allergen] = set(ingredients)

while len(correspondances.keys())>0:
    for key in correspondances.keys() :
        if len(correspondances[key])==1 :
            ing = list(correspondances[key])[0]
            matchs[key]=ing
            for key in correspondances.keys() :
                correspondances[key].discard(ing)
    dicoKeys = list(correspondances.keys())
    for key in dicoKeys:
        if len(correspondances[key])==0 :
            correspondances.pop(key)

print(matchs)

counter = 0
for line in lines :
    splitted = line.split(" ")
    ingredients = splitted[0:splitted.index("(contains")]
    for ingredient in ingredients :
        if not ingredient in matchs.values() :
            counter +=1

print(",".join([matchs[x] for x in (sorted(list(matchs.keys())))]))