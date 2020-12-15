from functools import reduce  # Required in Python 3
import operator

ingredients =[
    [2,0,-2,0],
    [0,5,-3,0],
    [0,0,5,-1],  
    [0,-1,0,5]
]

def calories(index) :
   return 3+(index//2)*5

recipe = [0,0,0,0]
def addList(list1,list2):
    if list1 == None :
        return list2
    elif list2 == None :
        return list1
    else :
        return [a + b for a, b in zip(list1,list2)]

def prod(iterable):
    if not sum(n < 0 for n in iterable) :
        return reduce(operator.mul, iterable, 1)
    else:
        return 0

def mult(l,x):
    return [i*x for i in l]


lowCabs = [addList(mult(ingredients[0],i),mult(ingredients[1],60-i)) for i in range(0,61)]
highCabs = [addList(mult(ingredients[2],i),mult(ingredients[3],40-i)) for i in range(0,41)]

#max l1 + l for l in l2
def maxProd(l1,l2) :
    return max(
        list(
            map(
                lambda l : prod(addList(l1,l)),
                l2
                )
            )
        )

print(max([maxProd(l,highCabs) for l in lowCabs]))