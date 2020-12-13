import re
f = open("input")
lines = f.readlines()
f.close()

timestamp=int(lines[0].strip('\n'))
busList = list(map(int,re.findall("\d+", lines[1])))
print(busList)
timeBeforeBus = list(map(lambda bus : bus - (timestamp % bus),busList))
print(timeBeforeBus)
position = timeBeforeBus.index(min(timeBeforeBus))
print(busList[position],timeBeforeBus[position],busList[position]*timeBeforeBus[position])
