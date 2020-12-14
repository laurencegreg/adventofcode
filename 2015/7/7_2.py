import re
f = open("input")
lines = f.readlines()
f.close()

values ={}
binOperations=[]

class BinOperation :
    def __init__(self,op,varName,dictVar) :
        self.op=op
        self.varName=varName
        self.dictVar ={}
        self.varOrder = []
        self.resolved = False
        for var in dictVar :
            if var.isdigit() :
                self.dictVar[var]=int(var)
            else :
                self.dictVar[var]= None if not (var in values.keys()) else values[var]
            self.varOrder.append(var)
    
    def refresh(self) :
        for var in self.dictVar.keys():
            if (var in values.keys()) :
                self.dictVar[var]=values[var]
        if not None in self.dictVar.values():
            self.compute()
    
    def compute (self):
        self.resolved = True
        if self.op == "AND" :
            values[self.varName]=self.dictVar[self.varOrder[0]]&self.dictVar[self.varOrder[1]]
        elif self.op == "OR" :
            values[self.varName]=self.dictVar[self.varOrder[0]]|self.dictVar[self.varOrder[1]]
        elif self.op == "LSHIFT" :
            values[self.varName]=self.dictVar[self.varOrder[0]]<<self.dictVar[self.varOrder[1]]
        elif self.op == "RSHIFT" :
            values[self.varName]=self.dictVar[self.varOrder[0]]>>self.dictVar[self.varOrder[1]]
        elif self.op == "NOT":
            values[self.varName]=~self.dictVar[self.varOrder[0]]+65536
        else : 
            values[self.varName]=self.dictVar[self.varOrder[0]]
    
    def __str__ (self):
        return "<"+self.op+" "+str(self.varOrder)+" -> "+self.varName+">\n"

    def __repr__(self):
        return self.__str__()


for line in lines :
    var = re.findall("[a-z]+|\d+",line)
    op = re.findall("[A-Z]+", line)
    if not op :
        if var[0].isdigit() :
            values[var[1]]=int(var[0])
            print(var[0],var[1])
        else :
            binOperations.append(BinOperation("SET",var[-1],var[:-1]))
    else :
        binOperations.append(BinOperation(op[0],var[-1],var[:-1]))

values["b"]=956

def step(stepValues):
    global binOperations
    global values
    print(values)
    for it in range(0,len(binOperations)):
        binOperations[it].refresh()
    binOperations = list(filter(lambda x: not x.resolved, binOperations))
    if stepValues != list(values) :
        step(list(values))


step(list(values))

print(values["a"])
