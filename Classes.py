from random import choice, randint, sample
import Data


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
        self.full_hp = self.full_hp - (damage -
                                       damage * self.final_protection())

    def is_alive(self):
        if self.full_hp <= 0:
            return False
        else:
            return True


class Paladin(Person):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.name = name * 2
        self.defense = defense * 2


class Warrior(Person):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.attack = attack * 2


class Arena:
    POSSIBLE_CLASSES = {
        'Paladin': Paladin,
        'Warrior': Warrior
    }

    def create_random_thing(self,
                            adjective=choice(Data.ADJECTIVE_THINGS),
                            name=choice(Data.THINGS)):
        full_name = adjective + name
        new_thing = Thing(full_name,
                          Data.VALUES['random_thing_hp'],
                          Data.VALUES['random_thing_attack'],
                          Data.VALUES['random_thing_defense'])
        return new_thing

    def create_random_character(self,
                                adjective=choice(Data.ADJECTIVE_NAMES),
                                name=choice(Data.NAMES)
                                ):
        cls = choice(list(Arena.POSSIBLE_CLASSES.keys()))
        full_name = name + adjective
        attack = Data.VALUES['random_character_attack']
        defense = Data.VALUES['random_character_defense']
        hp = Data.VALUES['random_character_hp']
        character = Arena.POSSIBLE_CLASSES[cls](full_name, hp, attack, defense)
        return character

    def create_bots_with_things(self, number_of_things, number_of_bots):
        list_of_things = [self.create_random_thing()
                          for _ in range(number_of_things)]
        list_of_things.sort(key=lambda x: x.defense)
        list_of_bots = [self.create_random_character()
                        for _ in range(number_of_bots)]
        for obj in list_of_bots:
            num_of_things_per_bot = randint(1, 4)
            things_per_bot = sample(list_of_things, num_of_things_per_bot)
            obj.set_things(things_per_bot)
        return list_of_bots

    def bots_battle(self, list_of_participants):
        while len(list_of_participants) > 1:
            couple = sample(list_of_participants, 2)
            index0 = list_of_participants.index(couple[0])
            index1 = list_of_participants.index(couple[1])

            damage = list_of_participants[index1].attack_damage()
            list_of_participants[index0].take_damage(damage)
            attacker = list_of_participants[index1].name
            defender = list_of_participants[index0].name
            print(f'{attacker} наносит удар по '
                  f'{defender} на {damage} урона')
            if not list_of_participants[index0].is_alive():
                list_of_participants.pop(index0)
        winner = list_of_participants[0].name
        print(f'{winner} - победитель')