import random
from things import Armour, Droid, Holocron, Ring
from people import Paladin, Warrior


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

