from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

init = lines[0].strip('\n').split(',')

def hash(st):
    res = 0
    for c in st:
        res = (res+ord(c))*17%256
    return res

boxes = []
for i in range(0,256):
    boxes.append({})
boxes[0]['a']=2
boxes[0].pop('a',None)

for st in init :
    if '-' in st:
        label = st.split('-')[0]
        boxes[hash(label)].pop(label,None)
    else :
        label = st.split('=')[0]
        focal = int(st.split('=')[1])
        boxes[hash(label)][label]=focal

fin = 0
for id,box in enumerate(boxes):
    for i,k in enumerate(box.keys()):
        fin +=(id+1)*(i+1)*box[k]
print(fin)