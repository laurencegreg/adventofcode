from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

map =[]
path = []
pos = []

for line in lines :
    if "#" in line :
        map.append(list(line.strip('\n').replace("#","##").replace(".","..").replace("@","@.").replace("O","[]"))) 
        if "@" in line :
            y = len(map)-1
            pos=[map[y].index('@'),y]
    elif line != "\n":
        path += list(line.strip('\n'))
for l in map:
    print("".join(l))
dir = {'>':[1,0],'^':[0,-1],'<':[-1,0],'v':[0,1]}

def valMove(l,r,xi,yi):
    if yi == 0:
        #move left
        if xi == -1:
            c = map[l[1]][l[0]-1]
            return c == '.' or (c ==']' and valMove([l[0]-2,l[1]],[r[0]-2,r[1]],xi,yi))
        #move right
        if xi == 1:
            c = map[r[1]][r[0]+1]
            return c == '.' or (c =='[' and valMove([l[0]+2,l[1]],[r[0]+2,r[1]],xi,yi))
        #move up
    else:
        if yi == -1 :
            tmp = True
            cl = map[l[1]-1][l[0]]
            cr = map[r[1]-1][r[0]]
            if cl=='#' or cr =='#':
                tmp = False
            elif cl =='[' :
                tmp = tmp and valMove([l[0],l[1]-1],[r[0],r[1]-1],xi,yi)
            else :
                if cl == ']':
                    tmp = tmp and valMove([l[0]-1,l[1]-1],[r[0]-1,r[1]-1],xi,yi)
                if cr == '[':
                    tmp = tmp and valMove([l[0]+1,l[1]-1],[l[0]+2,l[1]-1],xi,yi)
            return tmp
        if yi == 1 :
            tmp = True
            cl = map[l[1]+1][l[0]]
            cr = map[r[1]+1][r[0]]
            if cl=='#' or cr =='#':
                tmp = False
            elif cl =='[' :
                tmp = tmp and valMove([l[0],l[1]+1],[r[0],r[1]+1],xi,yi)
            else :
                if cl == ']':
                    tmp = tmp and valMove([l[0]-1,l[1]+1],[r[0]-1,r[1]+1],xi,yi)
                if cr == '[':
                    tmp = tmp and valMove([l[0]+1,l[1]+1],[r[0]+1,r[1]+1],xi,yi)
            return tmp


def move(l,r,xi,yi):
    if yi == 0:
        #move left
        if xi == -1:
            c = map[l[1]][l[0]-1]
            if c ==']':
                move([l[0]-2,l[1]],[r[0]-2,r[1]],xi,yi)
            map[l[1]][l[0]-1]=map[l[1]][l[0]]
            map[l[1]][l[0]]=map[r[1]][r[0]]
        #move right
        if xi == 1:
            c = map[r[1]][r[0]+1]
            if c =='[':
                move([l[0]+2,l[1]],[r[0]+2,r[1]],xi,yi)
            map[r[1]][r[0]+1]=map[r[1]][r[0]]
            map[r[1]][r[0]]=map[l[1]][l[0]]
    else:
        #move up
        if yi == -1 :
            cl = map[l[1]-1][l[0]]
            cr = map[r[1]-1][r[0]]
            if cl=='[':
                move([l[0],l[1]-1],[r[0],r[1]-1],xi,yi)
            if cl == ']':
                move([l[0]-1,l[1]-1],[r[0]-1,r[1]-1],xi,yi)
                map[l[1]-1][l[0]-1]="."
            if cr == '[':
                move([l[0]+1,l[1]-1],[l[0]+2,l[1]-1],xi,yi)
                map[r[1]-1][r[0]+1]="."
            map[l[1]-1][l[0]]=map[l[1]][l[0]]
            map[r[1]-1][r[0]]=map[r[1]][r[0]]
        #move down
        if yi == 1 :
            cl = map[l[1]+1][l[0]]
            cr = map[r[1]+1][r[0]]
            if cl =='[' :
                move([l[0],l[1]+1],[r[0],r[1]+1],xi,yi)
            if cl == ']':
                move([l[0]-1,l[1]+1],[r[0]-1,r[1]+1],xi,yi)
                map[l[1]+1][l[0]-1]="."
            if cr == '[':
                move([l[0]+1,l[1]+1],[r[0]+1,r[1]+1],xi,yi)
                map[r[1]+1][r[0]+1]="."
            map[l[1]+1][l[0]]=map[l[1]][l[0]]
            map[r[1]+1][r[0]]=map[r[1]][r[0]]
            
for step in path:
    d = dir[step]
    next = [pos[0]+d[0],pos[1]+d[1]]
    if map[next[1]][next[0]]==".":
        map[pos[1]][pos[0]]="."
        map[next[1]][next[0]]="@"
        pos=next
    elif map[next[1]][next[0]]=="[":
        if valMove(next,[next[0]+1,next[1]],d[0],d[1]):
            move(next,[next[0]+1,next[1]],d[0],d[1])
            map[pos[1]][pos[0]]="."
            map[next[1]][next[0]]="@"
            if d[0]==0 :
                map[next[1]][next[0]+1]="."
            pos=next
    elif map[next[1]][next[0]]=="]":

        if valMove([next[0]-1,next[1]],next,d[0],d[1]):
            move([next[0]-1,next[1]],next,d[0],d[1])
            map[pos[1]][pos[0]]="."
            map[next[1]][next[0]]="@"
            if d[0]==0 :
                map[next[1]][next[0]-1]="."
            pos=next


for l in map:
    print("".join(l))


res = 0
for y in range(0,len(map)):
    for x in range(0,len(map[y])):
        if map[y][x]=='[':
            res += 100*y+x
print(res)