import re
f = open("input")
lines = f.readlines()
f.close()

player1 =[]
player2 =[]
it = 1
while lines[it].strip("\n") != "" :
    player1.append(int(lines[it].strip("\n")))
    it+=1

it+=2
for line in lines[it:]:
    player2.append(int(line.strip("\n")))

while len(player1) != 0 and len(player2) != 0 :
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1 > card2 :
        player1.append(card1)
        player1.append(card2)
    else :
        player2.append(card2)
        player2.append(card1)

print(player2)
print(len(player2))
counter = 0
for i in range(0,len(player2)) :
    counter += (i+1)*player2[len(player2)-i-1]
    print((i+1),"*",player2[len(player2)-i-1])

print(counter)