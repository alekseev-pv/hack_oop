from typing import List, Tuple, Optional
import random


class Thing:
    """Вещи модифицирующие характеристики персонажа"""

    def __init__(
        self,
        name: str,
        hit_points: float = 0,
        protection: float = 0,
        attack_damage: float = 0,
    ):
        self.name = name
        self.hit_points = hit_points
        self.protection = protection
        self.attack_damage = attack_damage


class Person:
    def __init__(
        self,
        name: str,
        hit_points: float,
        protection: float,
        attack_damage: float,
    ):
        self.name = name

        self.hit_points = hit_points
        self.final_hit_points = hit_points

        self.protection = protection
        self.final_protection = protection

        self.attack_damage = attack_damage
        self.final_attack_damage = attack_damage

        self.things: Optional[List[Thing]] = None

    def set_things(self, things: List[Thing]):
        self.things = things

        bonus_protection = sum([thing.protection for thing in self.things])
        self.final_protection = self.protection + bonus_protection

        bonus_attack_damage = sum(
            [thing.attack_damage for thing in self.things]
        )
        self.final_attack_damage = self.attack_damage + bonus_attack_damage

        bonus_hit_points = sum([thing.hit_points for thing in self.things])
        self.final_hit_points = self.hit_points + bonus_hit_points

    def subtract_hit_points(self, attack_damage: float):
        self.final_hit_points -= (
            attack_damage - attack_damage * self.final_protection
        )

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}"

    def __repr__(self):
        return self.__str__()


class Paladin(Person):
    def __init__(
        self,
        name: str,
        hit_points: float,
        protection: float,
        attack_damage: float,
    ):
        super().__init__(name, hit_points * 2, protection * 2, attack_damage)


class Warrior(Person):
    def __init__(
        self,
        name: str,
        hit_points: float,
        protection: float,
        attack_damage: float,
    ):

        super().__init__(name, hit_points, protection, attack_damage * 2)


class PersonsGenerator:
    MAX_HIT_POINT = 150
    MIN_HIT_POINT = 50
    MAX_PROTECTION = 0.4
    MIN_PROTECTION = 0.0
    MAX_ATTACK_DAMAGE = 40
    MIN_ATTACL_DAMAGE = 5
    CLASSES: Tuple[Paladin, Warrior] = (Paladin, Warrior)

    def __init__(self, names: List[str]):
        self.names = names

    def get_hero(self):
        name = random.choice(self.names)
        hit_points = random.randint(self.MIN_HIT_POINT, self.MAX_HIT_POINT)
        protection = random.uniform(self.MIN_PROTECTION, self.MAX_PROTECTION)
        attack_damage = random.randint(
            self.MIN_ATTACL_DAMAGE, self.MAX_ATTACK_DAMAGE
        )

        random_class = random.choice(self.CLASSES)
        hero = random_class(name, hit_points, protection, attack_damage)
        return hero


class Arena:
    MIN_THINGS = 1
    MAX_THINGS = 4

    def __init__(self, persons: List[Person], things: List[Thing]):
        self.persons = persons
        self.things = things

    def equip_randomly(self):
        for person in self.persons:
            number_equip = random.randint(self.MIN_THINGS, self.MAX_THINGS)
            things = random.choices(self.things, k=number_equip)
            person.set_things(things)
