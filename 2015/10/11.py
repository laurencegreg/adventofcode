
input = "vzbxkghb"

def step(input):
    result=[]
    current = input[0]
    counter = 1
    for char in input[1:] :
        if char == current :
            counter+=1
        else :
            result.append(str(counter))
            result.append(current)
            counter=1
            current=char
    result.append(str(counter))
    result.append(current)
    return result

for i in range(0,50):
    input=step(input)

print(len(input))