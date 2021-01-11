class Node :
    def __init__(self,value) :
        self.value=value
        self.following=None
    
    def __repr__(self):
        return self.__str__
    
    def __str__(self):
        return self.value + "->" + (self.following.value if self.following else "None")
    
input = "942387615"
first = Node(input[0])
current = first
for char in input[1:] :
    following=Node(char)
    current.following = following
    current=following
current.following = first



def printChain(current) :
    value = current.value
    output = value
    current = current.following
    while current != None and current.value != value :
        output+="->"+current.value
        current=current.following
    return output


def remove(current):
    following = current.following
    last = following.following.following
    current.following = last.following
    last.following=None
    return(current,following)


def nextNode(current):
    find=False
    value=int(current.value)-1
    while value >0 and not find :
        step = current.following
        while step != current and not find :
            if step.value == str(value) :
                find=True
            else :
                step=step.following
        if not find :
            value -=1
    if find :
        return step
    else :
        step = current.following
        maxNode = step
        while step != current :
            step = step.following
            if step.value > maxNode.value :
                maxNode = step
        return maxNode

def insertElement(pos,ins):
    nextNode = pos.following
    pos.following = ins
    step = ins.following
    while step.following != None :
        step = step.following
    step.following = nextNode

current = first
def step(current):
    (c,f)=(remove(current))
    destination = nextNode(c)
    insertElement(destination,f)
    return current.following

for i in range(0,100) :
    current = step(current)

while current.value != "1" :
    current = current.following

print(printChain(current).replace("->",""))