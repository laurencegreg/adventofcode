import re
import math
f = open("input")
lines = f.readlines()
f.close()

class Piece :
    def __init__ (self,name):
        self.name = name
        self.repr = []
        self.matched = {}
        self.borders = {}

    def __repr__ (self):
        res = ""
        for line in self.repr :
            res += line+"\n"
        return res

    def __str__(self):
        return self.__repr__()

    def build(self):
        self.borders = {}
        self.addDirection(self.repr[0],"north")
        self.addDirection(self.repr[0][::-1],"revnorth")
        self.addDirection(self.repr[-1],"south")
        self.addDirection(self.repr[-1][::-1],"revsouth")
        west = "".join([line[0] for line in self.repr]) 
        self.addDirection(west,"west")
        self.addDirection(west[::-1],"revwest")
        east = "".join([line[-1] for line in self.repr])
        self.addDirection(east,"east")
        self.addDirection(east[::-1],"reveast")

    def wrong(self):
        transformed = ["".join(["." for i in range(0,len(self.repr))]) for j in range(0,len(self.repr))]
        self.repr = transformed

    def rotating180 (self):
        transformed = [[None for i in range(0,len(self.repr))] for j in range(0,len(self.repr))]
        for i in range(0,len(transformed)) :
            laligne = ""
            for j in range(0,len(transformed[0])) :
                laligne +=self.repr[len(self.repr)-1-i][len(self.repr)-1-j]
            transformed[i]=laligne
        self.repr = transformed
    
    def rotating90 (self):
        transformed = [[None for i in range(0,len(self.repr))] for j in range(0,len(self.repr))]
        for i in range(0,len(transformed)) :
            laligne = ""
            for j in range(0,len(transformed[0])) :
                laligne +=self.repr[len(self.repr)-1-j][i]
            transformed[i]=laligne
        self.repr = transformed
    
    def rotating270 (self):
        transformed = [[None for i in range(0,len(self.repr))] for j in range(0,len(self.repr))]
        for i in range(0,len(transformed)) :
            laligne = ""
            for j in range(0,len(transformed[0])) :
                laligne +=self.repr[j][len(self.repr)-1-i]
            transformed[i]=laligne
        self.repr = transformed

    def flipping (self):
        transformed = [self.repr[len(self.repr)-1-j] for j in range(0,len(self.repr))]
        self.repr = transformed

    def flippingH (self):
        transformed = [self.repr[i][::-1] for i in range(0,len(self.repr))]
        self.repr = transformed

    def addDirection (self,path,dir):
        if not path in self.borders.keys() :
            self.borders[path]=[dir]
        else :
            self.borders[path].append(dir)


    def match(self,piece) :
        matches = set(self.borders.keys()).intersection(set(piece.borders.keys()))
        for match in matches :
            for pos in self.borders[match] :
                self.addMatch(pos,piece.name,piece.borders[match])
            for pos in piece.borders[match] :
                piece.addMatch(pos,self.name,self.borders[match])

    def addMatch (self,myPos,pieceName,piecePos):
        if not myPos in self.matched.keys() :
            self.matched[myPos]=[(pieceName,piecePos)]
        else :
            self.matched[myPos].append((pieceName,piecePos))
pieces = []
currentPiece = None
for line in lines :
    if re.search("\d+",line):
        if currentPiece != None :
            currentPiece.build()
            pieces.append(currentPiece)
        currentPiece = Piece(str(re.findall("\d+", line)[0]))
    elif line != "\n" :
        currentPiece.repr.append(line.strip("\n"))

currentPiece.build()
pieces.append(currentPiece)

matchedPieces = {}
while len(pieces)>0 :
    computedPiece = pieces.pop()
    for piece in pieces :
        computedPiece.match(piece)
    matchedPieces[computedPiece.name]=computedPiece

res = 1

#    print(piece.name,set([s.replace("rev","") for s in piece.matched.keys()]))
#    print(set(re.findall("\d+", str(piece.matched.values()))))

# liste des voisins
for piece in matchedPieces.values() :
    piece.neighbours = list(set(re.findall("\d+", str(piece.matched.values()))))

#initialisation du tableau
size = int(math.sqrt(len(matchedPieces.keys())))
tableau = [[None for i in range(0,size)] for j in range(0,size)]

tableau[0][0]=matchedPieces["3457"]
matched="2287"
piece = matchedPieces[matched]
piece.neighbours =  list(filter(lambda x: x != tableau[0][0].name,piece.neighbours))
tableau[0][1] = piece
tableau[0][0].neighbours = list(filter(lambda x: x != matched,tableau[0][0].neighbours))
#parcour diagonal chelou
# [0, 1, 4, 7, 12, 17, 24, 31, 40, 49, 60, 71]
# [2, 3, 6, 11, 16, 23, 30, 39, 48, 59, 70, 83]
# [5, 8, 10, 15, 22, 29, 38, 47, 58, 69, 82, 93]
# [9, 13, 18, 21, 28, 37, 46, 57, 68, 81, 92, 103]
# [14, 19, 25, 32, 36, 45, 56, 67, 80, 91, 102, 111]
# [20, 26, 33, 41, 50, 55, 66, 79, 90, 101, 110, 119]
# [27, 34, 42, 51, 61, 72, 78, 89, 100, 109, 118, 125]
# [35, 43, 52, 62, 73, 84, 94, 99, 108, 117, 124, 131]
# [44, 53, 63, 74, 85, 95, 104, 112, 116, 123, 130, 135]
# [54, 64, 75, 86, 96, 105, 113, 120, 126, 129, 134, 139]
# [65, 76, 87, 97, 106, 114, 121, 127, 132, 136, 138, 141]
# [77, 88, 98, 107, 115, 122, 128, 133, 137, 140, 142, 143]

position = (1,0)
moving = (1,-1)
diag = 0
pair = True

def findPiece(position) :
    (x,y)=position
    close = []
    if x-1 >= 0 :
        close.append(tableau[x-1][y])
    if y-1 >= 0 :
        close.append(tableau[x][y-1])
    matched = set.intersection(*list(map(lambda piece : set(piece.neighbours),close))).pop()
    piece = matchedPieces[matched]
    piece.neighbours =  list(filter(lambda x: not x in (list(map(lambda x : x.name,close))),piece.neighbours))
    for p in close :
        p.neighbours = list(filter(lambda x: x != matched,p.neighbours))
    tableau[x][y]=piece


        
    

while not size in position :
    findPiece(position)
    (x,y)=position
    (i,j)=moving
    if x+i < 0 or y+j == size:
        if not pair :
            position =(diag+1,diag-1)
        else :
            position =(diag+1,diag)
        moving = (1,-1)
    elif y+j < 0 or x+i == size :
        if not pair :
            position = (diag,diag+1)
            pair = True
        else :
            pair = False
            diag +=1
            position = (diag,diag)
        moving = (-1,1)
    else :
        position = (x+i,y+j)


# for i in range(0,len(tableau)) :
#     for j in range(0,len(tableau[0])) :
#         piece = tableau[i][j]
#         south = tableau[i+1][j].name if i+1<len(tableau) else ""
#         north = tableau[i-1][j].name if i != 0 else ""
#         east = tableau[i][j+1].name if j+1<len(tableau) else ""
#         west = tableau[i][j-1].name if j != 0 else ""
#         model = [".",".",".","."]
#         for match in piece.matched.keys() :
#             (id,_) =piece.matched[match][0]

#             if id == north and not "rev" in match:
#                 model[0]=match[0]
#             elif id == south and not "rev" in match:
#                 model[1]=match[0]
#             elif id == east and not "rev" in match:
#                 model[2]=match[0]
#             if id == west and not "rev" in match :
#                 model[3]=match[0]
#         model = "".join(model)
#         print(piece.name)
#         if re.search(model,"snew") :
#             print("flip")
#             piece.flipping()
#         elif re.search(model,"ewsn") :
#             print("90")
#             piece.rotating90()
#         elif re.search(model,"snwe") :
#             print("180")
#             piece.rotating180()
#         elif re.search(model,"wens") :
#             print("270")
#             piece.rotating270()
#         elif re.search(model,"nsew") :
#             print("normal")
#         else :
#             print("**********WRONG*******")
#             piece.wrong()



matchedPieces["3457"].rotating180()

for j in range(1,len(tableau[0])) :
    neighb = tableau[0][j-1]
    eastLine ="".join([line[-1] for line in neighb.repr])
    piece = tableau[0][j]
    while eastLine != piece.repr[-1] and eastLine[::-1] != piece.repr[-1] :
        piece.rotating90()
    if eastLine == piece.repr[-1] :
        piece.rotating90()
    else :
        piece.rotating90()
        piece.flipping()
for j in range(0,len(tableau)) :
    for i in range (1,len(tableau[i])) :
        neighb = tableau[i-1][j]
        southLine = neighb.repr[-1]
        piece = tableau[i][j]
        while piece.repr[0] != southLine and piece.repr[0]!= southLine[::-1] :
            piece.rotating90()
        if piece.repr[0] == southLine[::-1] :
            piece.flippingH()





for line in tableau :
    lineTab = ["" for i in range(0,len(line[0].repr)+1)]
    for piece in line :
        for il in range(0,len(piece.repr)) :
            lineTab[il] += piece.repr[il]+" "
        lineTab[-1]+="......"+piece.name+" "

    for x in lineTab :
        print(x)
    print("")

finalTab = []
for line in tableau :
    lineTab = ["" for i in range(1,len(line[0].repr)-1)]
    for piece in line :
        for il in range(1,len(piece.repr)-1) :
            lineTab[il-1] += piece.repr[il][1:-1]
    finalTab.extend(lineTab)

def snake(t,position):
    (x,y) = position
    return (t[x][y]=="#" 
    and t[x+1][y+1]=="#" 
    and t[x+1][y+4]=="#" 
    and t[x][y+5]=="#" 
    and t[x][y+6]=="#" 
    and t[x+1][y+7]=="#" 
    and t[x+1][y+10]=="#" 
    and t[x][y+11]=="#" 
    and t[x][y+12]=="#" 
    and t[x+1][y+13]=="#"
    and t[x+1][y+16]=="#" 
    and t[x][y+17]=="#" 
    and t[x][y+18]=="#" 
    and t[x-1][y+18]=="#" 
    and t[x][y+19]=="#")

def flipping(t) :
    return [t[len(t)-1-j] for j in range(0,len(t))]

def rotating90(t):
    transformed = [[None for i in range(0,len(t))] for j in range(0,len(t))]
    for i in range(0,len(transformed)) :
        laligne = ""
        for j in range(0,len(transformed[0])) :
            laligne +=t[len(t)-1-j][i]
        transformed[i]=laligne
    return transformed

finalTab = rotating90(finalTab)
finalTab = flipping(finalTab)

for line in finalTab :
    print(line)
counter = sum(list(map(lambda x : x.count("#"),finalTab)))
print(counter)
for i in range(0,len(finalTab)-1):
    for j in range(0,len(finalTab[i])-19) :
        if snake(finalTab,(i,j)) :
            print(i,j)
            counter-=15

print(counter)

