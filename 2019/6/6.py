import re
f = open("input")
lines = f.readlines()
f.close()


class Universe :
    def __init__(self):
        self.planets={}
    
    def addPlanet(self,planet):
        self.planets[planet.name]=planet
    
    def nbOrbits(self,planetName):
        if planetName in self.planets.keys() :
            return self.nbOrbits(self.planets[planetName].orbits)+1
        else :
            return 0
    
    def allOrbits(self):
        return sum(list(map(lambda planet : self.nbOrbits(planet.name),self.planets.values())))

class Planet :
    def __init__(self,name,orbits):
        self.name = name
        self.orbits = orbits

universe = Universe()
for line in lines :
    splitted = line.strip("\n").split(")")
    universe.addPlanet(Planet(splitted[1],splitted[0]))

print(universe.allOrbits())