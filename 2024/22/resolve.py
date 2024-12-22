from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

def step (secret):
    scrt = secret
    tmp = scrt*64
    scrt = tmp^scrt
    scrt = scrt%16777216
    tmp = scrt//32
    scrt = tmp^scrt
    scrt = scrt%16777216
    tmp = scrt*2048
    scrt = tmp^scrt
    scrt = scrt%16777216
    return scrt
secrets = list(map(lambda x: int(x.strip('\n')),lines))
for i in range (0,2000):
    secrets = list(map(step,secrets))

print(sum(secrets))