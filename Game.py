"""
Игра арена
(Основана по мотивам 'The Elder Scrolls: Arena' 1994г.)

На арене будут сражаться все известные вам персонажи, от простых купцов
до богов и даэдра. Вам остается делать ставки кто выживет в бою, а кто проиграет.

"""
import random as rd
from random import randint
from operator import attrgetter


class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.hp: int = 10
        self.attack: int = 1
        self.protect: int = 0
        self.things = []

    def setThing(self, thing) -> None:
        self.things.append(thing)
        self.hp += thing.bonus_hp
        self.attack += thing.bonus_attack
        self.protect += thing.bonus_protect

    def get_damaged(self, attack_damage) -> None:
        self.hp = round(self.hp - attack_damage - attack_damage*(self.protect/100), 2)


    def statusHero(self) -> str:
        output: str = 'Имя {}, здоровье {}, атака {}, защита {}%.'.format(self.name, self.hp, self.attack, self.protect)
        return output

class Thing:
    def __init__(self) -> None:
        self.bonus_hp: int = randint(0, 3)
        self.bonus_attack: int = randint(0, 4)
        self.bonus_protect: int = rd.randint(0, 10)


class Paladin(Person):
    def __init__(self, name) -> None:
        Person.__init__(self, name)
        self.hp = self.hp * 2
        self.protect = self.protect * 2

    def status(self) -> str:
        return self.statusHero()

class Warrior(Person):
    def __init__(self, name) -> None:
        Person.__init__(self, name)
        self.attack = self.attack * 2

    def status(self) -> str:
        return self.statusHero()


def fight(heroes):
    while len(heroes) > 1:
        dual = rd.sample(heroes, k=2)
        attack = dual.pop(randint(0,1))
        defender = dual.pop()
        defender.get_damaged(attack.attack)
        print('{} наносит удар по {} на {} урона'.format(attack.name, defender.name, attack.attack))
        if defender.hp < 0:
            heroes.remove(defender)
    
    if len(heroes) == 1:
        winner = heroes.pop()
        return('Побеидил {}! У него осталось {} здоровья'.format(winner.name, winner.hp))
    else:
        return('Все погибли, никто не победил!')


name_of_hero = ["Азура", "Боэтия", "Вермина", "Джиггалаг", "Клавикус", "М'Айк", "Малакат", "Меридия", "Мерунес Дагон", "Мефала", "Молаг Бал", "Намира", "Ноктюрнал", "Периайт", "Сангвин", "Ситис", "Уриэль Септим", "Хермеус Мора", "Хирсин", "Шеогорат"]
bonus_things = sorted([Thing() for _ in range(20)], key=lambda thing: thing.bonus_protect)
heroes_paladin = [Paladin(rd.choice(name_of_hero)) for _ in range(10)]
heroes_warrior = [Warrior(rd.choice(name_of_hero)) for _ in range(10)]
heroes = heroes_paladin + heroes_warrior
for hero in heroes:
    for bonus_thing in rd.sample(bonus_things, k=randint(1,4)):
        hero.setThing(bonus_thing)

print(fight(heroes))
