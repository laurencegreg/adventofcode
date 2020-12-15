import re
f = open("input")
lines = f.readlines()
f.close()

cities = {}

class City :
    def __init__(self):
        self.reachable = {}
    
    def setDest (self,city,length):
        self.reachable[city]=length
    
    def travel (self,alreadyVisited,lengthPath):
        dest = set(self.reachable.keys())-alreadyVisited
        if len(dest)==0 :
            return lengthPath if len(alreadyVisited) == len(cities.keys()) else None
        else :
            distances = []
            for city in dest :
                visited = alreadyVisited.copy()
                visited.add(city)
                distance = cities[city].travel(visited,lengthPath+self.reachable[city])
                if distance != None :
                    distances.append(distance)
            return min(distances)
    
    def __str__ (self):
        return "<"+str(self.reachable)+">\n"

    def __repr__(self):
        return self.__str__()

for line in lines :
    splitted = line.split("=")
    length = int(splitted[1].strip('\n'))
    lineCities = splitted[0].strip().split(" to ")
    for c in lineCities :
        if not c in cities.keys() :
            cities[c]=City()
    cities[lineCities[0]].setDest(lineCities[1],length)
    cities[lineCities[1]].setDest(lineCities[0],length)

distances=[]
for city in cities.keys():
    distances.append(cities[city].travel(set([city]),0))

print(min(distances))
