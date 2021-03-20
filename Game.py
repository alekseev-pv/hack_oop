"""
Игра "Арена"
(Основана по мотивам 'The Elder Scrolls: Arena' 1994г.)

На арене будут сражаться все известные вам персонажи, от простых купцов
до богов и даэдра. Вам остается делать ставки кто выживет в бою, а кто проиграет.

"""
import random as rd
import colorama

from colorama import Fore, Back, Style
from random import randint
from operator import attrgetter


class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.hp: float = 10
        self.attack: float = 1
        self.protect: float = 0
        self.things = []

    def setThing(self, thing) -> None:
        self.things.append(thing)
        self.hp += thing.bonus_hp
        self.attack += thing.bonus_attack
        self.protect += thing.bonus_protect

    def get_damaged(self, attack_damage) -> None:
        self.hp = round(self.hp - attack_damage - attack_damage*(self.protect/100), 2)


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


class Warrior(Person):
    def __init__(self, name) -> None:
        Person.__init__(self, name)
        self.attack = self.attack * 2


class Orc(Person):
    def __init__(self, name) -> None:
        Person.__init__(self, name)
        self.hp = self.hp * 1.5


class Thief(Person):
    def __init__(self, name) -> None:
        Person.__init__(self, name)
        self.attack = self.attack * 2.5
        self.hp = self.hp - 2


def fight(heroes) -> str:
    while len(heroes) > 1:
        dual = rd.sample(heroes, k=2)
        attack = dual.pop(randint(0,1))
        defender = dual.pop()
        defender.get_damaged(attack.attack)
        print('{} наносит удар по {} на {} урона'.format(attack.name, defender.name, attack.attack))
        if defender.hp < 0:
            colorama.init()
            print(Fore.RED + '{} получает смертельное ранение и погибает (но т.к. он даэдра, с ним все хорошо)'.format(defender.name), end="")
            print(Style.RESET_ALL)
            heroes.remove(defender)
    
    if len(heroes) == 1:
        winner = heroes.pop()
        return(Fore.YELLOW + 'Победил {}!'.format(winner.name))
    else:
        return(Fore.RED + 'Все погибли, никто не победил!')


def creation_of_heroes(name_of_hero, bonus_things) -> list:
    heroes = [Paladin(rd.choice(name_of_hero)) for _ in range(5)]
    heroes += [Warrior(rd.choice(name_of_hero)) for _ in range(5)]
    heroes += [Orc(rd.choice(name_of_hero)) for _ in range(5)]
    heroes += [Thief(rd.choice(name_of_hero)) for _ in range(5)]
    for hero in heroes:
        for bonus_thing in rd.sample(bonus_things, k=randint(1,4)):
            hero.setThing(bonus_thing)
    return heroes

name_of_hero = ["Азура", "Боэтия", "Вермина", "Джиггалаг", "Клавикус", "М'Айк", "Малакат", "Меридия", "Мерунес Дагон", "Мефала", "Молаг Бал", "Намира", "Ноктюрнал", "Периайт", "Сангвин", "Ситис", "Уриэль Септим", "Хермеус Мора", "Хирсин", "Шеогорат"]
bonus_things = sorted([Thing() for _ in range(20)], key=lambda thing: thing.bonus_protect) #сортировка вещей по защите

print(fight(creation_of_heroes(name_of_hero, bonus_things)))
print(Style.RESET_ALL)
