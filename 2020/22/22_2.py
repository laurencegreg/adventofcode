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

def recGame(player1,player2,tab) :
    states=set()
    states.add(",".join(list(map(str,player1)))+"|"+",".join(list(map(str,player2))))
    rec = False
    tabSpaces = "".join(["   " for i in range(0,tab)])
    while len(player1) != 0 and len(player2) != 0 and not rec :
        print(tabSpaces+"--------------")
        print(tabSpaces+"Player 1's deck:",player1)
        print(tabSpaces+"Player 2's deck:",player2)
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        print(tabSpaces+"Player 1 plays:",card1)
        print(tabSpaces+"Player 2 plays:",card2)
        if len(player1)>=card1 and len(player2)>=card2 :
            (res,_,_) =recGame(player1[:card1],player2[:card2],tab+1)
            if res :
                print(tabSpaces+"Player 1 wins Game")
                player1.append(card1)
                player1.append(card2)
            else :
                print(tabSpaces+"Player 2 wins Game")
                player2.append(card2)
                player2.append(card1)
        else :
            if card1 > card2 :
                print(tabSpaces+"Player 1 wins")
                player1.append(card1)
                player1.append(card2)
            else :
                print(tabSpaces+"Player 2 wins")
                player2.append(card2)
                player2.append(card1)
        state = ",".join(list(map(str,player1)))+"|"+",".join(list(map(str,player2)))
        if state in states :
            print(tabSpaces+"--------------")
            print(tabSpaces+"already seen state "+state)
            print(tabSpaces+"end of subGame : player 1 win")
            rec = True
        else :
            states.add(state)
        print(tabSpaces+"--------------")

    return (rec or len(player1)>0,player1,player2)

(res,player1,player2) = recGame(player1,player2,0)


counter = 0
for i in range(0,len(player2)) :
    counter += (i+1)*player2[len(player2)-i-1]
    print((i+1),"*",player2[len(player2)-i-1])

print(counter)