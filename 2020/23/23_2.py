class Node :
    def __init__(self,value) :
        self.value=value
        self.following=None
    
    def __repr__(self):
        return self.__str__
    
    def __str__(self):
        return self.value + "->" + (self.following.value if self.following else "None")


dicoNodes = {}
removed = []
input = "942387615"
first = Node(input[0])
dicoNodes[input[0]]=first
current = first
for char in input[1:]:
    following=Node(char)
    dicoNodes[char]=following
    current.following = following
    current=following
for i in range(10,1000001):
    following=Node(str(i))
    dicoNodes[str(i)]=following
    current.following = following
    current=following
current.following=first


def printChain(current) :
    value = current.value
    output = value
    current = current.following
    while current != None and current.value != value :
        output+="->"+current.value
        current=current.following
    return output

def remove(current):
    global removed
    following = current.following
    removed = [following.value,following.following.value,following.following.following.value]
    last = following.following.following
    current.following = last.following
    last.following=None
    return(current,following)

# def remove(current):
#     global removed
#     removed=[]
#     step = current
#     last = None
#     following = None
#     it = 3
#     while it>=0 :
#         if step.tail :
#             nextValue = int(step.value)+1
#             if nextValue != 1000000 :
#                 newNode = Node(str(int(step.value)+1))
#                 dicoNodes[newNode.value]=newNode
#                 newNode.tail=True
#                 step.following = newNode
#             else :
#                 step.following = million
#         step = step.following
#         if it==3 :
#             following = step
#         if it==1 :
#             last=step
#         if it != 0 :
#             removed.append(step.value)
#         it-=1
#     current.following = last.following
#     last.following=None 
#     return(current,following)

# def nextNode(current):
#     print(current)
#     find=False
#     value=int(current.value)-1
#     print(list(dicoNodes.keys()))
#     print(removed)
#     while value >0 and not find :
#         step = current.following
#         while step != current and not step.tail and not find :
#             if step.value == str(value) :
#                 find=True
#             else :
#                 step=step.following
#         if not find :
#             value -=1
#     if find :
#         print(step)
#         return step
#     else :
#         print(million)
#         return million

def nextNode(current):
    find=False
    value=int(current.value)-1 if int(current.value)>1 else 1000000
    strValue=str(value)
    while not find :
        if not strValue in removed :
            find = True
        else :
            value= value-1 if value>1 else 1000000
            strValue=str(value)
    return dicoNodes[strValue]



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

for i in range(0,10000000) :
    current = step(current)



print(dicoNodes["1"],dicoNodes["1"].following)