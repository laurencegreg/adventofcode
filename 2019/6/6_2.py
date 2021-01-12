import re
f = open("input")
lines = f.readlines()
f.close()


class Universe :
    def __init__(self):
        self.planets={}
    
    def addPlanet(self,planet):
        self.planets[planet.name]=planet
    
    def reverseOrbits(self,planetName,revDico,it):
        revDico[planetName]=it
        if planetName in self.planets.keys() :
            return self.reverseOrbits(self.planets[planetName].orbits,revDico,it+1)
        else :
            return revDico


class Planet :
    def __init__(self,name,orbits):
        self.name = name
        self.orbits = orbits

universe = Universe()
for line in lines :
    splitted = line.strip("\n").split(")")
    universe.addPlanet(Planet(splitted[1],splitted[0]))

dicoYou = universe.reverseOrbits("YOU",{},0)
dicoSan = universe.reverseOrbits("SAN",{},0)
value = min(list(map(lambda x : dicoYou[x],list(set(dicoYou.keys())&dicoSan.keys()))))
firstCommonOrbit = [x for x in dicoYou.keys() if dicoYou[x]==value][0]

print(dicoYou[firstCommonOrbit]+dicoSan[firstCommonOrbit]-2)