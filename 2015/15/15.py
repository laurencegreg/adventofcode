from functools import reduce  # Required in Python 3
import operator

ingredients =[
    [2,0,-2,0],
    [0,5,-3,0],
    [0,0,5,-1],  
    [0,-1,0,5]
]

recipe = [0,0,0,0]
def addList(list1,list2):
    return [a + b for a, b in zip(list1,list2)]

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

recipe = addList(recipe,ingredients[0])
recipe = addList(recipe,ingredients[1])
recipe = addList(recipe,ingredients[2])
recipe = addList(recipe,ingredients[2])
recipe = addList(recipe,ingredients[3])

def step(recipe) :
    result = addList(recipe,ingredients[0])
    for i in range(1,4):
        tmp = addList(recipe,ingredients[i])
        if prod(tmp)>prod(result) :
            result=tmp
    return result

for i in range(0,95):
    recipe=step(recipe)

print(recipe,prod(recipe))