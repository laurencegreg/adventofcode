from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

def score (counter):
    mc = counter.most_common(2)
    big = mc[0][1]
    if big==5 :
        return 'a'
    elif big==4 :
        return 'b'
    elif big==3 :
        if mc[1][1]==2:
            return 'c'
        else :
            return 'd'
    elif big == 2 :
        if mc[1][1]==2:
            return 'e'
        else :
            return 'f'
    else : 
        return 'g'

hands = []
for line in lines : 
    sp = line.split(' ')
    hand = sp[0]
    ar = list(hand)
    ar.sort()
    scoreAr = str(score(Counter(ar)))
    mapCard = hand.maketrans("AKQJT98765432","abcdefghijklm")
    mapped = hand.translate(mapCard)
    # [hand,bet,sortKey]
    hands.append([sp[0],int(sp[1]),scoreAr+mapped])

hands.sort(key=lambda x:x[2])

print(hands)
def res(idx_and_item):
    index,item = idx_and_item
    return (len(hands)-index)*item[1]
print(sum(map(res,enumerate(hands))))
