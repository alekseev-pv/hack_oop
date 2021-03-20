from random import choice, uniform, randint
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

    def set_things(self, thing):
        self.things.append(thing)

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
        self.hp = self.hp - (damage - damage * self.final_protection())

    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True


class Paladin(Person):
    def __init__(self, name, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.name = name * 2
        self.defense = defense * 2


class Warrior(Person):
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.defense = defense
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
