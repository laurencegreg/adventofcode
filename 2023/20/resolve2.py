from collections import Counter
import re
f = open("input")
lines = f.readlines()
f.close()


class Flip:
    def __init__(self,name,rec):
        self.name = name
        self.on = False
        self.receivers = rec
    
    def addSender (self,sender):
        None
    
    def receipt(self,pulse,sender):
        if pulse == "high" :
            return []
        else :
            self.on = not self.on
            call = []
            for r in self.receivers :
                call.append([self.name,r,"high" if self.on else "low"])
            return call

class Conjunction:
    def __init__(self,name,rec):
        self.name = name
        self.last = "low"
        self.receivers = rec
        self.senders = {}
    
    def addSender (self,sender):
        self.senders[sender]="low"

    def receipt(self,pulse,sender):
        self.senders[sender]=pulse
        sendPulse =  "high" if "low" in self.senders.values() else "low"
        call = []
        for r in self.receivers :
            call.append([self.name,r,sendPulse])
        return call


modules = {}
tmpSenders = []
broadcaster = []
for line in lines :
    sp = line.strip('\n').split(" -> ")
    if '%' in sp[0]:
        modules[sp[0][1:]]=Flip(sp[0][1:],sp[1].split(", "))
        tmpSenders.extend(list(map(lambda x : [sp[0][1:],x],sp[1].split(", "))))
    elif '&' in sp[0]:
        modules[sp[0][1:]]=Conjunction(sp[0][1:],sp[1].split(", "))
        tmpSenders.extend(list(map(lambda x : [sp[0][1:],x],sp[1].split(", "))))
    else:
        broadcaster = sp[1].split(", ")
        tmpSenders.extend(list(map(lambda x : [sp[0],x],sp[1].split(", "))))

for s in tmpSenders:
    if s[1] in modules:
        modules[s[1]].addSender(s[0])




counters={'low':0,'high':0}

found = False
i =0
while not found: 
    #button
    pulses = list(map(lambda x : ['broadcaster',x,'low'],broadcaster))
    counters['low']+=1
    while len(pulses)!=0 :
        pulse = pulses.pop(0)
        counters[pulse[2]]+=1
        if pulse[1] in modules:
            pulses.extend(modules[pulse[1]].receipt(pulse[2],pulse[0]))
        else :
            found = pulse[2]=='low'
    i+=1
    if i%100000 == 0 :
        print(i)

print(i)