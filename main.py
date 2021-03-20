

class Thing:

    def __init__(self, things_name, thing_protection, thing_attack, thing_life):
        self.things_name = things_name
        self.thing_protection = thing_protection
        self.thing_attack = thing_attack
        self.thing_life = thing_life


class Person:

    def __init__(self, pers_name, pers_life, pers_attack, pers_protection):
        self.pers_name = pers_name
        self.pers_life = pers_life
        self.pers_attack = pers_attack
        self.pers_protection = pers_protection
    
    def setThings(self, things):
        pass

    def subtract_life(self):
        pass
    

class Paladin(Person):

    def __init__(self, pers_name, pers_life, pers_attack, pers_protection):
        super().__init__(pers_name, pers_attack)
        self.pers_life = pers_life * 2
        self.pers_protection = pers_protection * 2


class Warrior(Person):

    def __init__(self, pers_name, pers_life, pers_attack, pers_protection):
        super().__init__(pers_name, pers_life, pers_protection)
        self.pers_attack = pers_attack * 2
