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
        self.hp = hp
        self.things = []
        self.full_hp = hp

    def set_one_thing(self, thing):
        self.things.append(thing)
        # Временное решение для здоровья предмета
        self.full_hp += thing.hp

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
        self.hp = hp * 2
        self.defense = defense * 2


class Warrior(Person):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.attack = attack * 2


class Witcher(Person):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.attack = attack * 2
        self.hp = hp * 2

        self.things = [Thing('Ведьмачий медальон', 3, 1, 0.02)]


class Arena:
    POSSIBLE_CLASSES = {
        'Paladin': Paladin,
        'Warrior': Warrior,
        'Witcher': Witcher
    }

    def create_random_thing(self):
        adjective = choice(Data.ADJECTIVE_THINGS)
        name = choice(Data.THINGS)
        full_name = adjective + name
        # new_thing = Thing(full_name,
        #                   Data.VALUES['random_thing_hp'],
        #                   Data.VALUES['random_thing_attack'],
        #                   Data.VALUES['random_thing_defense'])
        new_thing = Thing(full_name,
                          randint(1, 5),
                          randint(2, 5),
                          float('{:.2f}'.format(uniform(0.01, 0.05))))
        return new_thing

    def create_random_character(self):
        name = choice(Data.NAMES)
        adjective = choice(Data.ADJECTIVE_NAMES)

        cls = choice(list(Arena.POSSIBLE_CLASSES.keys()))
        full_name = name + adjective
        # attack = Data.VALUES['random_character_attack']
        # defense = Data.VALUES['random_character_defense']
        # hp = Data.VALUES['random_character_hp']
        attack = randint(8, 13)
        defense = float('{:.2f}'.format(uniform(0.1, 0.2)))
        hp = randint(40, 55)
        character = Arena.POSSIBLE_CLASSES[cls](full_name, hp, attack, defense)
        return character

    def create_bots_with_things(self, number_of_things, number_of_bots):
        list_of_things = []
        for _ in range(number_of_things):
            obj = Arena()
            list_of_things.append(obj.create_random_thing())

        list_of_things.sort(key=lambda x: x.defense)

        list_of_bots = []
        for _ in range(number_of_bots):
            obj = Arena()
            list_of_bots.append(obj.create_random_character())

        for obj in list_of_bots:
            num_of_things_per_bot = randint(1, 3)
            things_per_bot = sample(list_of_things, num_of_things_per_bot)
            obj.set_things(things_per_bot)
        return list_of_bots

    def bots_battle(self, list_of_participants):
        colorama.init()
        print(Fore.MAGENTA + 'Представляем участников сегодняшней битвы!' +
              Style.RESET_ALL)
        for obj in list_of_participants:
            print(f'{Fore.CYAN + obj.name + Style.RESET_ALL} со своим '
                  f'снаряжением: ' + Fore.YELLOW)
            for i in range(len(obj.things)):
                if i == len(obj.things) - 1:
                    print(obj.things[i].name + Style.RESET_ALL)
                else:
                    print(obj.things[i].name, end='; ')

        while len(list_of_participants) > 1:
            couple = sample(list_of_participants, 2)
            index0 = list_of_participants.index(couple[0])
            index1 = list_of_participants.index(couple[1])

            damage = list_of_participants[index1].attack_damage()
            final_damage = list_of_participants[index0].take_damage(damage)

            attacker = list_of_participants[index1].name
            defender = list_of_participants[index0].name
            hp = list_of_participants[index0].full_hp
            if hp < 0:
                hp = 0
            print(f'{Fore.MAGENTA + attacker + Style.RESET_ALL} '
                  f'наносит удар по '
                  f'{Fore.CYAN + defender + Style.RESET_ALL} '
                  f'на {Fore.RED + str(final_damage) + Style.RESET_ALL} урона, у '
                  f'{Fore.CYAN + defender + Style.RESET_ALL} '
                  f'остается {Fore.GREEN + str(hp) + Style.RESET_ALL} '
                  f'ед. здоровья')
            if not list_of_participants[index0].is_alive():
                print(colorama.Fore.RED +
                      f'{defender}'
                      f' погибает!')
                print(colorama.Style.RESET_ALL)

                list_of_participants.pop(index0)
        winner = list_of_participants[0].name
        print(f'{Fore.GREEN + winner + Style.RESET_ALL} - победитель')
