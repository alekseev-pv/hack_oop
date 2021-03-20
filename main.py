class Person:
    def __init__(self):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
    
    def SetThings(self, things):
        pass

    def SubtractHealth(self, attack):
        pass

class Paladin(Person):
    def __init__(self):
        self.defence = self.defence * 2
    pass

class Warrior(Person):
    def __init__(self):
        self.attack = self.attack * 2


