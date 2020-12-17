f = open("armory")
lines = f.readlines()
f.close()

class Stuff :
    def __init__ (self,name,cost,damage,defense):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.defense = defense
    
    def __str__ (self):
        return "<"+self.name+" : "+str(self.damage)+"/"+str(self.defense)+" ("+str(self.cost)+"$)>"
    
    def __repr__(self):
        self.__str__

class Ring(Stuff) :
    kind = "ring"

class Weapon(Stuff) :
    kind = "weapon"

class Armor(Stuff) :
    kind = "armor"


class Armory :
    def __init__(self):
        self.weapons=set()
        self.armors=set()
        self.rings=set()
    
    def __str__ (self):
        return "<weapons>\n"+str(self.weapons)+"\n<armors>\n"+str(self.armors)+"\n<rings>\n"+str(self.rings)
    
    def __repr__(self):
        self.__str__

class Person :
    def __init__ (self,name,basicAttack,basicDefense):
        self.name = name
        self.points = 100
        self.armor = None
        self.weapon = None
        self.rings = []
        self.attack = basicAttack
        self.defense = basicDefense

    def __str__ (self):
        return "<"+self.name+" : "+str(self.points)+"health>\n"+"<attack : "+self.getAttack()+" defense : "+self.getDefense()+">\n<rings : "+str(self.rings)+">"
    
    def __repr__(self):
        self.__str__

    def addStuff(self,stuff):
        if stuff.kind == "armor" :
            if self.armor :
                self.defense-=self.armor.defense
            self.armor=stuff
            self.defense+=stuff.defense
            
        if stuff.kind == "weapon" :
            if self.weapon :
                self.attack-=self.weapon.damage
            self.weapon=stuff
            self.attack+=stuff.damage

        if stuff.kind == "ring" :
            if len(self.rings)<2 :
                self.rings.append(stuff)
                self.defense+=stuff.defense
                self.attack+=stuff.attack
            else :
                print("already too many rings")

    def heal(self):
        self.points=100
    
    def defense(self,points) :
        self.points-=max(points-self.defense,1)
    
    def attack(self,person) :
        person.defense(self.attack)

    def removeRing(self,position):
        if position==0 :
            self.rings = [self.rings[1]]
        else:
            self.rings = [self.rings[0]]

                
