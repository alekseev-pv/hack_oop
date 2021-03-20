from typing import List, Optional, Tuple
import random


class Thing:
    def __init__(self, name: str, hp: float = 0,
                 damage: float = 0, protection: float = 0):
        self.name = name
        self.protection = protection
        self.damage = damage
        self.hp = hp


class Person:
    def __init__(self, name: str, hp: float, damage: float, protection: float):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.protection = protection
        self.things: Optional[List[Thing]] = None

    def set_things(self, things: List[Thing]):
        self.things = things

    def attack_damage(self):
        damage = self.attack
        for obj in self.things:
            damage += obj.attack
        return damage

    def final_protection(self):
        protection = self.protection
        for obj in self.things:
            protection += obj.protection
        return protection

    def damage_received(self, damage):
        self.hp = self.hp - (damage - damage * self.final_protection)

    def life(self):
        if self.hp <= 0:
            return False
        return True


class Fighter(Person):
    def __init__(self, name: str, hp: float, damage: float, protection: float):
        super().__init__(name, hp, damage, protection)


class Paladin(Person):
    def __init__(self, name: str, hp: float, damage: float, protection: float):
        super().__init__(name, hp * 2, damage / 2, protection * 2)


class Warrior(Person):
    def __init__(self, name: str, hp: float, damage: float, protection: float):
        super().__init__(name, hp / 2, damage * 2, protection / 2)


class Person_generator:
    Min_HP = 250
    Max_HP = 500
    Min_protection = 0.0
    Max_protection = 0.5
    Min_damage = 20
    Max_damage = 45
    Classes: Tuple[Fighter, Paladin, Warrior] = (Fighter, Paladin, Warrior)
    Names = [
        "Aaron",
        "Saimon",
        "Wolter",
        "Westheimer",
        "Emilia",
        "Kratos",
        "Robert",
        "Mara",
        "Ceasar",
        "Ahmad",
    ]

    def __init__(self, names: List[str]):
        self.names = names

    def create_person(self, name) -> Person:
        hp = random.randint(self.Min_HP, self.Max_HP)
        protect = random.uniform(self.Min_protection, self.Max_protection)
        damage = random.randint(self.Min_damage, self.Max_damage)
        random_class = random.choice(self.Classes)
        person = random_class(name, hp, protect, damage)
        return person

    def create_persons(self, persons_number: int = None) -> List[Person]:
        persons_number = len(
            self.names) if persons_number is None else persons_number
        names = random.choices(self.names, k=persons_number)
        return [self.create_person(name) for name in names]
