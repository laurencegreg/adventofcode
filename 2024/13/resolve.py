from collections import Counter
import re
f = open("input.test")
lines = f.readlines()
f.close()



def resolve(x,y,ax,ay,bx,by):
    print(str(x)+','+str(y)+','+str(ax)+','+str(ay)+','+str(bx)+','+str(by))
    found = False
    i=0
    while not(found) and ax*i<x:
        tmpX = x-ax*i
        tmpY = y-ay*i
        if tmpX%bx==0 and tmpY%by==0 and tmpX//bx==tmpY//by :
            found=True
            print(i)
            print(tmpX//bx)
            return i*3 + tmpX//bx
        i+=1
    return 0


buttons = {}
res = 0
for line in lines :
    if "Button" in line:
        #Button A: X+94, Y+34
        sp = line.strip().split(' ')
        buttons[sp[1][:-1]]=[int(sp[2][2:-1]),int(sp[3][2:])]
    elif "Prize" in line :
        #Prize: X=8400, Y=5400
        sp = line.strip().split(' ')
        res+=resolve(int(sp[1][2:-1]),int(sp[2][2:]),buttons["A"][0],buttons["A"][1],buttons["B"][0],buttons["B"][1])

print(res)