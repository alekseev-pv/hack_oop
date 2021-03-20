from random import randint

names_heroes = ['Shakira', 'Beyomce', 'Kim kardashyan', 'Britney',
                'Terminator', 'Rembo', 'Kuyan', 'Byure',
                'Stifler', 'Born', 'Perevozchik', 'Toreto',
                'CHak_Norris', 'Pupisenok', 'Harley Queen', 'Bear',
                'Torin duboshit', 'Gendalf', 'Potter', 'Hermiona']


class Thing:
    """The objects of this class are helmets, pants, gloves, robes, swords"""
    def __init__(self, name: str = 'player', armor: int = 0, atack: int = 0,
                 health: int = 0) -> None:
        self.name = name
        self.armor = armor
        self.atack = atack
        self.health = health


class Person(Thing):
    """The class for wariors"""
    def __init__(self, name, armor, atack, health):
        """Init takes from class Thing"""
        super().__init__(name, armor, atack, health)
        self.bagage = []
        self.equiped = [self.name, self.armor, self.atack, self.health]

    def setthings(self, things):
        self.bagage.append(things)

    def armored_health(self):
        for items in self.bagage:
            self.equiped[1] = self.equiped[1] + items[1]
            self.equiped[2] = self.equiped[2] + items[2]
            self.equiped[3] = self.equiped[3] + items[3]

    def health_damage(self, damage):
        self.equiped[3] = (self.equiped[3] -
                           damage + damage * self.equiped[1] / 100)
        print(self.name + " получил " +
              str(damage - damage * self.equiped[1] / 100) +
              " повреждений, осталось здоровья " + str(self.equiped[3]))

    def game_atack(self, players):
        print(self.name + " атакует " + players.name)
        players.health_damage(self.equiped[2])


class Paladin(Person):
    def __init__(self, name, armor, atack, health):
        super().__init__(name, armor, atack, health)
        self.health = 2 * health


class Warrior(Person):
    def __init__(self, name, armor, atack, health):
        super().__init__(name, armor, atack, health)
        self.atack = 2 * atack


karmian_gloves = Thing('karmian gloves', 14)
ring_of_wisdom = Thing('ring of wisdom', 0, 0, 10)
brigandin_helmet = Thing('brigandin helmet', 12, 0, 0)
sword_of_valhala = Thing('sword of valhala', 0, 8, 0)
h1 = Paladin(names_heroes[randint(0, 19)], 2, 25, 100)
h2 = Paladin(names_heroes[randint(0, 19)], 2, 25, 100)
h3 = Paladin(names_heroes[randint(0, 19)], 2, 25, 100)
h4 = Paladin(names_heroes[randint(0, 19)], 2, 25, 100)
h5 = Paladin(names_heroes[randint(0, 19)], 2, 25, 100)
h6 = Warrior(names_heroes[randint(0, 19)], 2, 25, 100)
h7 = Warrior(names_heroes[randint(0, 19)], 2, 25, 100)
h8 = Warrior(names_heroes[randint(0, 19)], 2, 25, 100)
h9 = Warrior(names_heroes[randint(0, 19)], 2, 25, 100)
h10 = Warrior(names_heroes[randint(0, 19)], 2, 25, 100)
h1.setthings(karmian_gloves)
h2.setthings(ring_of_wisdom)
h3.setthings(brigandin_helmet)
h4.setthings(sword_of_valhala)
h5.setthings(karmian_gloves)
h6.setthings(ring_of_wisdom)
h7.setthings(brigandin_helmet)
h8.setthings(sword_of_valhala)
h9.setthings(karmian_gloves)
h10.setthings(ring_of_wisdom)
heroes = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]
while len(heroes) > 1:
    i = randint(0, (len(heroes) - 1))
    fighter1 = heroes[i]
    del heroes[i]
    j = randint(0, (len(heroes) - 1))
    fighter2 = heroes[j]
    del heroes[j]
    while fighter1.equiped[3] >= 0 and fighter2.equiped[3] >= 0:
        if randint(0, 1) == 0:
            fighter1.game_atack(fighter2)
        else:
            fighter2.game_atack(fighter1)
    if fighter1.equiped[3] > 0:
        heroes.append(fighter1)
    else:
        heroes.append(fighter2)
print('The winner is- ' + heroes[0].name)
