import re
f = open("input")
lines = f.readlines()
f.close()

data = lines[0].strip("\n")

def addLayer(image,layer):
    newImage=image.copy()
    for i in range(0,len(newImage)):
        for j in range(0,len(newImage[i])):
            layerPixel = layer[i*25+j]
            if layerPixel in ["0","1"]:
                newImage[i][j]=layerPixel
    return newImage


image=[["2" for x in range(0,25)] for y in range(0,6)]
for i in reversed(range(0,len(data)//(25*6))):
    image=addLayer(image,data[i*(25*6):(i+1)*(25*6)])

for line in list(map(lambda x : "".join(x).replace("0"," "),image)) :
    print(line)

