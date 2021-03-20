import random


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


class Person:
    """Base class for a character"""
    def __init__(self, name, hp, base_attack, base_def):
        self.name = name
        self.health = hp
        self.base_attack = base_attack
        self.base_defence = base_def
        self.things = []

    def set_things(self, things):
        self.things = things
        self.add_params()

    def get_hit(self, attacker):
        attack_damage = attacker.get_base_attack()
        final_protec = self.get_base_defence() / 100
        attack_damage -= attack_damage * final_protec
        attack_damage = round(attack_damage, 2)
        if self.health > 50 > self.health - attack_damage:
            if self.things:
                item = self.things.pop(0)
                self.base_attack -= item.attack
                self.base_defence -= item.defence
                self.health -= item.health
        self.health = self.health - attack_damage if self.health - attack_damage > 0 else 0
        self.health = round(self.health, 2)
        print(f'{attacker} наносит удар по {self.name} на {attack_damage} урона')


    def get_base_attack(self):
        return self.base_attack

    def get_base_defence(self):
        return self.base_defence

    def get_health(self):
        return self.health

    def add_params(self):
        add_attack = sum(t.attack for t in self.things)
        add_defence = sum(t.defence for t in self.things)
        add_health = sum(t.health for t in self.things)
        self.base_attack = self.base_attack + add_attack if self.base_attack + add_attack <= 110 else 110
        self.base_defence = self.base_defence + add_defence if self.base_defence + add_defence <= 110 else 110
        self.health = self.health + add_health if self.health + add_health <= 110 else 110

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Paladin(Person):
    def __init__(self, name, hp, base_attack, base_def):
        super().__init__(name, hp * 2, base_attack, base_def * 2)


class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_def):
        super().__init__(name, hp, base_attack * 2, base_def)


def generate(par: str):
    """This function takes a name of a class as a argument and generates random values for its members"""
    if par == 'Paladin':
        hp = random.randint(30, 35)
        base_attack = random.randint(60, 70)
        base_def = random.randint(30, 41)
    elif par == 'Warrior':
        hp = random.randint(60, 70)
        base_attack = random.randint(30, 35)
        base_def = random.randint(60, 82)
    return hp, base_attack, base_def


def get_name(names):
    """Gets a random name from the list"""
    name = random.choice(names)
    names.remove(name)
    return name


def get_dressed(fighters):
    """Dresses a fighter according to their level of base defence"""
    r1 = Ring('Green Ring')
    r2 = Ring('Red Ring')
    r3 = Ring('Blue Ring')
    r4 = Ring('Yellow Ring')
    r5 = Ring('Silver Ring')
    a1 = Armour('Mandalorian Armour')
    a2 = Armour('Red Armour')
    a3 = Armour('Green Armour')
    a4 = Armour('Blue Armour')
    a5 = Armour('Jedi Armour')
    a6 = Armour('Clone Armour')
    a7 = Armour('Aqua Armour')
    d1 = Droid('R5-D7')
    d2 = Droid('R3-D9')
    d3 = Droid('R4-D3')
    d4 = Droid('R9-D8')
    d5 = Droid('R3-D3')
    d6 = Droid('R5-D5')
    h1 = Holocron('Red')
    h2 = Holocron('Green')
    h3 = Holocron('Blue')
    h4 = Holocron('Silver')
    h5 = Holocron('Yellow')
    h6 = Holocron('Indigo')
    rings = [r1, r2, r3, r4, r5]
    armours = [a1, a2, a3, a4, a5, a6, a7]
    droids = [d1, d2, d3, d4, d5, d6]
    holocrons = [h1, h2, h3, h4, h5, h6]
    for fighter in fighters:
        things = []
        if fighter.get_base_defence() < 65:
            if armours:
                armour = random.choice(armours)
                armours.remove(armour)
                things.append(armour)
            if holocrons:
                holo = random.choice(holocrons)
                holocrons.remove(holo)
                things.append(holo)
            if droids:
                droid = random.choice(droids)
                droids.remove(droid)
                things.append(droid)
        elif fighter.get_base_defence() < 70:
            if armours:
                armour = random.choice(armours)
                armours.remove(armour)
                things.append(armour)
            if holocrons:
                holo = random.choice(holocrons)
                holocrons.remove(holo)
                things.append(holo)
        elif fighter.get_base_defence() < 70:
            if armours:
                armour = random.choice(armours)
                armours.remove(armour)
                things.append(armour)
            if holocrons:
                holo = random.choice(holocrons)
                holocrons.remove(holo)
                things.append(holo)
        elif fighter.get_base_defence() < 75:
            if holocrons:
                holo = random.choice(holocrons)
                holocrons.remove(holo)
                things.append(holo)
            if droids:
                droid = random.choice(droids)
                droids.remove(droid)
                things.append(droid)
            if rings:
                ring = random.choice(rings)
                rings.remove(ring)
                things.append(ring)
        else:
            if armours:
                armour = random.choice(armours)
                armours.remove(armour)
                things.append(armour)
            if rings:
                ring = random.choice(rings)
                rings.remove(ring)
                things.append(ring)
        if things:
            fighter.set_things(things)


def fight(fighters):
    fighters = fighters[:5]
    i = 0
    while len(fighters) > 1:
        attacker = random.choice(fighters)
        defender = random.choice(fighters)
        while attacker == defender:
            defender = random.choice(fighters)
        defender.get_hit(attacker)
        if defender.get_health() <= 0:
            fighters.remove(defender)
    print(f'{fighters[0]} won')

def main():

    names = ['Reuben', 'Noa', 'Ben', 'Plo', 'Simon', 'Mace', 'Ezra', 'Ari', 'Dave', 'Asoka', 'Ruth', 'Lea',
             'Cere', 'Eno', 'Rea', 'Debby', 'Dan', 'Caleb', 'Kit', 'Aalya']
    fighter1 = Warrior(get_name(names), *generate('Warrior'))
    fighter2 = Paladin(get_name(names), *generate('Paladin'))
    fighter3 = Warrior(get_name(names), *generate('Warrior'))
    fighter4 = Paladin(get_name(names), *generate('Paladin'))
    fighter5 = Warrior(get_name(names), *generate('Warrior'))
    fighter6 = Paladin(get_name(names), *generate('Paladin'))
    fighter7 = Warrior(get_name(names), *generate('Warrior'))
    fighter8 = Paladin(get_name(names), *generate('Paladin'))
    fighter9 = Warrior(get_name(names), *generate('Warrior'))
    fighter10 = Paladin(get_name(names), *generate('Paladin'))
    fighters = [fighter1, fighter2, fighter3, fighter4, fighter5,
                fighter6, fighter7, fighter8, fighter9, fighter10]
    fighters = sorted(fighters, key=lambda x: x.get_base_defence())
    get_dressed(fighters)
    fight(fighters)

if __name__ == "__main__":
    main()

