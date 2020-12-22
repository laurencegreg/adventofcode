import re
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

matchedPieces = []
while len(pieces)>0 :
    computedPiece = pieces.pop()
    for piece in pieces :
        computedPiece.match(piece)
    matchedPieces.append(computedPiece)

res = 1
for piece in matchedPieces :
    if len(set([s.replace("rev","") for s in piece.matched.keys()])) == 2 :
        print(piece.name)
        res *= int(piece.name)
print(res)