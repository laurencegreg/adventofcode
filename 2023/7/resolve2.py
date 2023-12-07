from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()

jocker = {}
jocker['a0']='a'
jocker['a5']='a'
jocker['b0']='b'
jocker['b1']='a'
jocker['b4']='a'
jocker['c0']='c'
jocker['c2']='a'
jocker['c3']='a'
jocker['d0']='d'
jocker['d1']='b'
jocker['d3']='b'
jocker['e0']='e'
jocker['e1']='c'
jocker['e2']='b'
jocker['f0']='f'
jocker['f1']='d'
jocker['f2']='d'
jocker['g0']='g'
jocker['g1']='f'

def score (counter):
    mc = counter.most_common(2)
    j = str(counter['J'])
    big = mc[0][1]
    if big==5 :
        return jocker['a'+j]
    elif big==4 :
        return jocker['b'+j]
    elif big==3 :
        if mc[1][1]==2:
            return jocker['c'+j]
        else :
            return jocker['d'+j]
    elif big == 2 :
        if mc[1][1]==2:
            return jocker['e'+j]
        else :
            return jocker['f'+j]
    else : 
        return jocker['g'+j]

hands = []
for line in lines : 
    sp = line.split(' ')
    hand = sp[0]
    ar = list(hand)
    ar.sort()
    scoreAr = str(score(Counter(ar)))
    mapCard = hand.maketrans("AKQT98765432J","abcdefghijklm")
    mapped = hand.translate(mapCard)
    # [hand,bet,sortKey]
    hands.append([sp[0],int(sp[1]),scoreAr+mapped])

hands.sort(key=lambda x:x[2])

def res(idx_and_item):
    index,item = idx_and_item
    return (len(hands)-index)*item[1]
print(sum(map(res,enumerate(hands))))
