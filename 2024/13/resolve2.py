from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()



def resolve(x,y,ax,ay,bx,by):
    #8400 (x) = 94 (ax) x + 22 (bx) y
    #5440 (y) = 34 (ay) x + 67 (by) y
    #x = 8400/94 (x/ax) - 22/94(bx/ax) y
    #x = 5440/34 (y/ay) - 67/34(by/ay) y
    # 8400/94 (x/ax) - 22/94(bx/ax) y = 5440/34 (y/ay) - 67/34(by/ay) y
    # 8400/94 (x/ax) - 5440/34 (y/ay) = (22/94(bx/ax) -67/34(by/ay)) y
    # y = (8400/94 (x/ax) - 5440/34 (y/ay))/(22/94(bx/ax) -67/34(by/ay))
    #y = ((8400*34-5400*94)/(94*34))/((22*34-67*94)/(34*94)
    #y  = ((8400*34-5400*94)/(94*34))*((94*34)/(22*34-67*94))
    #y = (8400*34-5400*94)/(22*34-67*94)
    #y = (x*ay - y*ax)/(bx*ay-by*ax)
    if (x*ay - y*ax)%(bx*ay-by*ax)==0:
        B = (x*ay - y*ax)//(bx*ay-by*ax)
        if (x - bx*B)%ax == 0:
            A = (x - bx*B)//ax
            return B+3*A
        else :
            return 0
    else :
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
        res+=resolve(10000000000000+int(sp[1][2:-1]),10000000000000+int(sp[2][2:]),buttons["A"][0],buttons["A"][1],buttons["B"][0],buttons["B"][1])

print(res)