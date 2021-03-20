"""
Игра "Арена"
(Основана по мотивам 'The Elder Scrolls: Arena' 1994г.)

Действия игры происходят на континенте Тамриэля, на планете Нирн (в переводе "Арена").
Происки злого мага Джагара Тарн не были бесчетными и привлекли к себе внимания всех принцев-даэдра.
Пока верный герой пытался остановить мага, собирая части Посоха Хаоса, Джагар Тарн не терял время
зря и нашел великое сердце Лорхана, с помощью которого он смог бы воссоздать великого Титана, но он был повержен,
а сердце осталось лежать в кромешной тьме, ожидая нового хозяина.

Прошло несколько лет с потери, но то ли судьба, то ли случайность в кромешной тьме глубокого подземелья
на сердце Лорхана наткнулся бродячий маг, чье пристрастие было путешествовать по кромешным подземельям в надежде найти
секреты новых заклинаний или неведанные книги новых знаний. Бродячего мага звали Тур Марн, он не представлял какой ценный
он нашел артефакт и взял его только ради алхимии: "Может пригодиться в опытах" промолвил он и уставший отправился на выход из подземелья.
Свои находки, которые ему удалось отыскать в подземелье Тур Марн решил отпраздновать в ближайшем дешевом баре. К сожалению, его 
любопытство к знаниям и тайнам было так же велико как и к выпивке. После двух бутылок дешевого вина и отвратительного на вкус, но
доступном по цене Мацт, маг отправился искать ночлежку в небольшой деревне Синагар, которая славилась своей вонючей рыбой и недружелюбностью к путникам.
Увы, но судьба мага не была блакосклонна к нему и в ближайшем переулке он был убит вором-новичком Укеном из Гильдии воров, молодой Каджит,
искавший как бы заработать на новую порцию лунного сахара. Продал он дорогую находку за недорого (нехватало даже на кусочек лунного сахара)
торговцу из Нелена, который выложил находку на самое видное место с целью поскорее продать. То ли на его счастье, а скорее нет эту находку случайно 
увидел принц-даэдра Сингвин и сразу начал договариваться с торговцев, но т.к. принц пропил последние гроши буквально вчера он не смог 
с ним договорится и отправился искать деньги на покупку. Но когда принц пришел, сердце уже было продано культистам принца Шеогората (принца
безумия) и от обиды Сингвин рассказал всем остальным принцам-даэдра об находке Шеогората. После этого началась великая борьба за сердце Лорхана,
между всеми принцами-даэдра, битва, которая унесла миллионы жизней.

Вы выступаете в роли Наблюдателя, вы обладаете абсолютным бессмертием, но...кроме как смотреть
ничего больше не можете...ваш создатель был не особо умен и мастером своего дела, но создавал вас с большой любовью. 
Вы можете делать ставки,болеть за ваших любимчиков. 

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

def decorate(fcn):
    def fight(name_of_hero, bonus_things) -> str:
        heroes = fcn(name_of_hero, bonus_things)
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
            print(Fore.YELLOW + 'Победил {}!'.format(winner.name))
        else:
            print(Fore.RED + 'Все погибли, никто не победил!')
    return fight

@decorate
def creation_of_heroes_and_fight(name_of_hero, bonus_things) -> list:
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

creation_of_heroes_and_fight(name_of_hero, bonus_things)
print(Style.RESET_ALL)
