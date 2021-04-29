import random
from typing import Dict, List
from .game_classes import Thing, Person


class ThingsGenerator:
    MAX_MULTIPLIER_HIT_POINTS = 1
    MIN_MULTIPLIER_HIT_POINTS = 0
    MAX_PROTECTION = 0.09
    MIN_PROTECTION = 0.0
    MAX_ATTACK_DAMAGE = 50
    MIN_ATTACK_DAMAGE = 0

    def __init__(self, names: List[str]):
        self.names = names

    def get_things(self):
        things = []
        for name in self.names:
            multiplier_hit_points = random.uniform(
                self.MIN_MULTIPLIER_HIT_POINTS, self.MAX_MULTIPLIER_HIT_POINTS
            )
            protection = random.uniform(
                self.MIN_PROTECTION, self.MAX_PROTECTION
            )
            attack_damage = random.randint(
                self.MIN_ATTACK_DAMAGE, self.MAX_ATTACK_DAMAGE
            )
            thing = Thing(
                name, multiplier_hit_points, protection, attack_damage
            )
            things.append(thing)
        return things


class NameGenerator:
    def __init__(self, nouns: List[Dict], subjects: List[str]):
        self.nouns = nouns
        self.subjects = subjects

    def get_names(self, number_names):
        nouns = random.choices(self.nouns, k=number_names)
        subjects = random.choices(self.subjects, k=number_names)

        return [f"{nouns[i]} {subjects[i]}" for i in range(number_names)]


class PersonsGenerator:
    MAX_HIT_POINT = 150
    MIN_HIT_POINT = 50
    MAX_PROTECTION = 0.2
    MIN_PROTECTION = 0.0
    MAX_ATTACK_DAMAGE = 40
    MIN_ATTACL_DAMAGE = 5

    def __init__(self, names: List[str], classes_persons: List[Person]):
        self.names = names
        self.classes_persons = classes_persons

    def get_person(self, name) -> Person:
        hit_points = random.randint(self.MIN_HIT_POINT, self.MAX_HIT_POINT)
        protection = random.uniform(self.MIN_PROTECTION, self.MAX_PROTECTION)
        attack_damage = random.randint(
            self.MIN_ATTACL_DAMAGE, self.MAX_ATTACK_DAMAGE
        )

        random_class = random.choice(self.classes_persons)
        person = random_class(name, hit_points, protection, attack_damage)
        return person

    def get_persons(self, number_persons: int = None) -> List[Person]:
        number_persons = (
            len(self.names) if number_persons is None else number_persons
        )
        names = random.choices(self.names, k=number_persons)

        return [self.get_person(name) for name in names]
