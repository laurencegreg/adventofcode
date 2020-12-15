import re
import itertools

f = open("input")
lines = f.readlines()
f.close()

class Reindeer :
    def __init__(self,name,speed,duration,sleep):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.sleep = sleep
        self.points=0
    
    def run(self,time) :
        return (time//(self.duration+self.sleep)*self.duration+min(self.duration,time%(self.duration+self.sleep)))*self.speed
    
    def addPoint(self) :
        self.points+=1

reindeers = {}

maximum = 0
for line in lines :
    values = list(map(int,(list(re.findall("\d+",line)))))
    name = line.split(" ")[0]
    reindeers[name]= Reindeer(name,values[0],values[1],values[2])


time = 2503
for i in range(1,time+1) :
    maxDist = 0
    winnersName = []
    for name in list(reindeers.keys()) :
        dist = reindeers[name].run(i)
        if dist > maxDist :
            maxDist = dist
            winnersName = [name]
        elif dist == maxDist :
            winnersName.append(name)
    for name in winnersName :
        reindeers[name].addPoint()

print(list(map(lambda name : reindeers[name].points,list(reindeers.keys()))))