from random import sample, random, randint
"""
У меня сегодня было мало свободного времени на хакатон (около 2 часов), 
но я все равно очень хотел поучаствовать:)
Соответственно, на рефакторинг времени совсем не было, многое можно сделать 
более оптимально.
Основное отличие от ТЗ - предметы влияют не только на защиту, но и на здоровье
(базовое здоровье пересчитывается после того, как предметы были надеты) и урон
(множитель урона от предметов учитывается в момент удара)
Вот, что получилось. 
"""


class Thing():
    def __init__(self, name, armor, damage, hp):
        self.name = name
        self.armor = armor
        self.damage = damage
        self.hp = hp


class Person():
    def __init__(self, name, base_hp, base_damage, base_armor):
        self.name = name
        self.base_hp = base_hp
        self.base_damage = base_damage
        self.base_armor = base_armor
        self.things = []

    def setThings(self, things):
        self.things = things

    def get_damage(self, damage):
        final_protection = (self.base_armor
                            + sum(thing.armor for thing
                                  in self.things))
        self.base_hp -= (damage - damage * final_protection)
        return damage - damage * final_protection


class Paladin(Person):
    def __init__(self, name, base_hp, base_damage, base_armor):
        super().__init__(name, base_hp, base_damage, base_armor)
        self.base_hp = 2 * base_hp
        self.base_armor = 2 * base_armor


class Warrior(Person):
    def __init__(self, name, base_hp, base_damage, base_armor):
        super().__init__(name, base_hp, base_damage, base_armor)
        self.base_damage = 2 * base_damage


if __name__ == "__main__":
    list_of_things = []
    for i in range(40):
        name = f'Вещь номер {i + 1}'
        armor = 0.1 * random()
        damage = 0.2 * random()
        hp = 0.1 * random()
        list_of_things.append(Thing(name=name, armor=armor, damage=damage,
                                    hp=hp))
    list_of_heroes = []
    for i in range(10):
        name = f'Герой номер {i + 1}'
        base_hp = 1000 * random()
        base_damage = 500 * random()
        base_armor = 0.1 * random()
        if random() > 0.5:
            list_of_heroes.append(Paladin(name=name,
                                          base_hp=base_hp,
                                          base_damage=base_damage,
                                          base_armor=base_armor)
                                  )
        else:
            list_of_heroes.append(Warrior(name=name,
                                          base_hp=base_hp,
                                          base_damage=base_damage,
                                          base_armor=base_armor)
                                  )
        things_quantity = round(4 * random())
        list_of_heroes[i].setThings(sample(list_of_things, things_quantity))
        if list_of_heroes[i].things:
            list_of_heroes[i].base_hp += sum(thing.hp for thing
                                             in list_of_heroes[i].things)

    counter = 10
    while counter > 1:
        attacker = randint(0, 9)
        defender = randint(0, 9)
        if (list_of_heroes[attacker].base_hp > 0
                and list_of_heroes[defender].base_hp > 0
                and attacker != defender):
            attack_damage = (list_of_heroes[attacker].base_damage
                             + list_of_heroes[attacker].base_damage *
                             sum(thing.damage for thing
                                 in list_of_heroes[attacker].things))
            final_damage = list_of_heroes[defender].get_damage(attack_damage)
            print(f'{list_of_heroes[attacker].name} наносит удар по '
                  f'{list_of_heroes[defender].name} на {final_damage} урона')
            if list_of_heroes[defender].base_hp <= 0:
                print(f'{list_of_heroes[defender].name} убит')
                counter -= 1

    for hero in list_of_heroes:
        if hero.base_hp > 0:
            print(f'{hero.name} выжил с {hero.base_hp} hp')