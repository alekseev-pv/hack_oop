from random import choice, randint, sample, uniform
import Data
import colorama
from colorama import Fore, Style
from math import floor


class Thing:

    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.hp = hp


class Person:

    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.things = []
        self.full_hp = hp

    def set_things(self, things_list):
        self.things += things_list
        for obj in things_list:
            self.full_hp += obj.hp

    def attack_damage(self):
        damage = self.attack
        for obj in self.things:
            damage += obj.attack
        return damage

    def final_protection(self):
        protection = self.defense
        for obj in self.things:
            protection += obj.defense
        return protection

    def take_damage(self, damage):
        full_damage = floor(damage - damage * self.final_protection())
        self.full_hp = self.full_hp - full_damage
        return full_damage

    def is_alive(self):
        if self.full_hp <= 0:
            return False
        else:
            return True


class Paladin(Person):

    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.full_hp = hp * 2
        self.defense = defense * 2


class Warrior(Person):

    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.attack = attack * 2


class Witcher(Person):

    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.attack = attack * 2
        self.full_hp = hp * 2

        # Ведьмак без ведьмачьего медальона - не ведьмак
        self.things = [Thing('Ведьмачий медальон', 3, 1, 0.02)]


class Arena:
    POSSIBLE_CLASSES = {
        'Paladin': Paladin,
        'Warrior': Warrior,
        'Witcher': Witcher
    }

    def create_random_thing(self):
        """Return Thing object with random parameters."""
        adjective = choice(Data.ADJECTIVE_THINGS)
        name = choice(Data.THINGS)
        full_name = adjective + name
        new_thing = Thing(full_name,
                          randint(1, 5),
                          randint(2, 5),
                          float('{:.2f}'.format(uniform(0.01, 0.05))))
        return new_thing

    def create_random_character(self):
        """Return Wither, Paladin or Warrior object with random parameters."""
        name = choice(Data.NAMES)
        adjective = choice(Data.ADJECTIVE_NAMES)
        full_name = name + adjective
        attack = randint(8, 13)
        defense = float('{:.2f}'.format(uniform(0.1, 0.2)))
        hp = randint(40, 55)

        # Случайный выбор одного из трех классов
        cls = choice(list(Arena.POSSIBLE_CLASSES.keys()))

        character = Arena.POSSIBLE_CLASSES[cls](full_name, hp, attack, defense)
        return character

    def create_bots_with_things(self, number_of_things, number_of_bots):
        """Return list of bot objects with not empty things list."""
        # Создание списка случайных предметов
        list_of_things = []
        for _ in range(number_of_things):
            obj = Arena()
            list_of_things.append(obj.create_random_thing())

        # Сортировка списка случайных предметов по ключу defense
        list_of_things.sort(key=lambda x: x.defense)

        # Создание списка случайныз персонажей
        list_of_bots = []
        for _ in range(number_of_bots):
            obj = Arena()
            list_of_bots.append(obj.create_random_character())

        # Выдача каждому персонажу случайного количества предметов
        for obj in list_of_bots:
            num_of_things_per_bot = randint(1, 3)
            things_per_bot = sample(list_of_things, num_of_things_per_bot)
            obj.set_things(things_per_bot)
        return list_of_bots

    def bots_battle(self, list_of_participants):
        """Generate battle between bots and print result of the battle"""
        # Инициализация модуля colorama
        colorama.init()

        # Вывод списка участников битвы с их вооружением
        print(Fore.MAGENTA + 'Представляем участников сегодняшней битвы!' +
              Style.RESET_ALL)
        for obj in list_of_participants:
            print(f'{Fore.CYAN + obj.name + Style.RESET_ALL}'
                  f' со своим снаряжением: ' + Fore.YELLOW)
            for i in range(len(obj.things)):
                if i == len(obj.things) - 1:
                    print(obj.things[i].name + Style.RESET_ALL)
                else:
                    print(obj.things[i].name, end='; ')

        # Попарное сражение в цикле, пока не останется один выживший
        while len(list_of_participants) > 1:
            # Выбор пары участников
            couple = sample(list_of_participants, 2)

            # Присовение индексов выбранной пары переменным index0 и index1
            index0 = list_of_participants.index(couple[0])
            index1 = list_of_participants.index(couple[1])

            # Рассчет получаемого урона с помощью вызова функций класса Person
            damage = list_of_participants[index1].attack_damage()
            final_damage = list_of_participants[index0].take_damage(damage)

            # Присовение имен атакующего и защищающегося для вывода на экран
            attacker = list_of_participants[index1].name
            defender = list_of_participants[index0].name

            # Исправение отрицательного показтеля здоровья для вывода на экран
            hp = list_of_participants[index0].full_hp
            if hp < 0:
                hp = 0

            # Вывод информации о текущем бое на экран
            print(f'{Fore.MAGENTA + attacker + Style.RESET_ALL} '
                  f'наносит удар по '
                  f'{Fore.CYAN + defender + Style.RESET_ALL} '
                  f'на {Fore.RED + str(final_damage) + Style.RESET_ALL}'
                  f' урона, у '
                  f'{Fore.CYAN + defender + Style.RESET_ALL} '
                  f'остается {Fore.GREEN + str(hp) + Style.RESET_ALL} '
                  f'ед. здоровья')

            # Удаление погибшего персонажа из списка участников битвы
            if not list_of_participants[index0].is_alive():
                print(colorama.Fore.RED +
                      f'{defender}'
                      f' погибает!')
                print(colorama.Style.RESET_ALL)
                list_of_participants.pop(index0)

        # Вывод имени победителя на экран
        winner = list_of_participants[0].name
        print(f'{Fore.GREEN + winner + Style.RESET_ALL} - победитель')
