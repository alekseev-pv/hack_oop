class Thing:
    """Base class for a useful item"""
    def __init__(self, name, attack, defence, health):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health

    def get_attack(self):
        return self.attack

    def get_defence(self):
        return self.defence

    def get_health(self):
        return self.health

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Ring(Thing):
    """Ring adds 30 points to health and 3 points to defence"""
    def __init__(self, name):
        super().__init__(name, 0, 5, 30)


class Armour(Thing):
    """Armour adds 10 points to defence and 5 points to health"""
    def __init__(self, name):
        super().__init__(name, 0, 10, 5)


class Droid(Thing):
    """Small flying battle droid, adds 30 points to attack and 5 points to defence"""
    def __init__(self, name):
        super().__init__(name, 30, 10, 0)


class Holocron(Thing):
    """An ancient artifact, adds 20 points to attack and health and 10 points to defence"""
    def __init__(self, name):
        super().__init__(name, 20, 10, 20)
