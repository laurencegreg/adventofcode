import re
f = open("input")
lines = f.readlines()
f.close()

data = lines[0].strip("\n")
layer=data[0:(25*6)]
minLayerZero = layer.count("0")
res = layer.count("1")*layer.count("2")
for i in reversed(range(1,len(data)//(25*6))):
    print("layer ",i)
    layer=data[i*(25*6):(i+1)*(25*6)]
    print("nb 0 : ",layer.count("0"))
    print("")
    if layer.count("0") < minLayerZero :
            minLayerZero = layer.count("0")
            res = layer.count("1")*layer.count("2")

print(minLayerZero)
print("res ",res)