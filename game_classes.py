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


class InventoryError(Exception):
    pass


class InventoryOverflowError(InventoryError):
    pass


class Inventory:
    def __init__(self, size: int):
        self.size = size
        self.things: List[Thing] = []

    def add_thing(self, thing: Thing) -> bool:
        if len(self.thing) >= self.size:
            return False
        self.things.append(thing)
        return True

    def set_things(self, things: List[Thing]):
        if len(self.things) > self.size:
            raise InventoryOverflowError
        self.things = [thing for thing in things]

    def remove_thing(self, index):
        self.things.pop(index)


class Person:
    MAX_SIZE_INVENTORY = 4

    def __init__(
        self,
        name: str,
        hit_points: float,
        protection: float,
        attack_damage: float,
    ):
        self.name = name

        self.hit_points = hit_points
        self.current_hit_points = hit_points
        self.final_hit_points = hit_points

        self.protection = protection
        self.final_protection = protection

        self.attack_damage = attack_damage
        self.final_attack_damage = attack_damage

        self.things: Optional[List[Thing]] = None
        self.inventory = Inventory(self.MAX_SIZE_INVENTORY)

    def update_characteristics(self):
        bonus_protection = sum(
            [thing.protection for thing in self.inventory.things]
        )
        self.final_protection = self.protection + bonus_protection

        bonus_attack_damage = sum(
            [thing.attack_damage for thing in self.inventory.things]
        )
        self.final_attack_damage = self.attack_damage + bonus_attack_damage

        bonus_hit_points = sum(
            [thing.hit_points for thing in self.inventory.things]
        )

        # для расчёта неполного здоровья при поднятии/снятии предмета
        # для коррекции текущего здоровья, расчитываеся разница между новым итоговы
        # и старым
        # нужено более элегантное решение
        new_final_hit_points = (
            self.hit_points + self.hit_points * bonus_hit_points
        )
        if self.final_hit_points != new_final_hit_points:
            correction_factor = new_final_hit_points / self.final_hit_points
            self.current_hit_points = (
                self.current_hit_points * correction_factor
            )
            self.final_hit_points = new_final_hit_points

    def set_inventory(self, things: List[Thing]):
        self.inventory.set_things(things)
        self.update_characteristics()

    def add_thing(self, thing: Thing):
        self.inventory.add_thing(Thing)
        self.update_characteristics()

    def reduce_hit_points(self, attack_damage: float) -> float:
        final_damage = attack_damage - attack_damage * self.final_protection
        final_damage = round(final_damage, 2)
        self.current_hit_points -= final_damage
        return final_damage

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

    def get_person(self, name) -> Person:
        hit_points = random.randint(self.MIN_HIT_POINT, self.MAX_HIT_POINT)
        protection = random.uniform(self.MIN_PROTECTION, self.MAX_PROTECTION)
        attack_damage = random.randint(
            self.MIN_ATTACL_DAMAGE, self.MAX_ATTACK_DAMAGE
        )

        random_class = random.choice(self.CLASSES)
        person = random_class(name, hit_points, protection, attack_damage)
        return person

    def get_persons(self, number_persons: int = None) -> List[Person]:
        number_persons = (
            len(self.names) if number_persons is None else number_persons
        )
        names = random.choices(self.names, k=number_persons)

        return [self.get_person(name) for name in names]


class Player:
    def __init__(
        self,
        name: str,
    ):
        self.name = name
        self.person: Optional[Person] = None

    def set_person(self, person: Person):
        self.person = person


class Arena:
    MIN_THINGS = 1
    MAX_THINGS = 4

    def __init__(self, persons: List[Person], things: List[Thing]):
        self.persons = persons
        self.things = things
        self.things.sort(key=lambda thing: thing.protection)

    def equip_randomly(self):
        for person in self.persons:
            number_equip = random.randint(self.MIN_THINGS, self.MAX_THINGS)
            things = random.choices(self.things, k=number_equip)
            person.set_inventory(things)

    def round_fight(self):
        couple_fighter = random.sample(self.persons, k=2)
        attacker: Person = couple_fighter[0]
        defender: Person = couple_fighter[1]
        damage = defender.reduce_hit_points(attacker.final_attack_damage)
        defender.final_hit_points = 0
        if defender.final_hit_points <= 0:
            self.persons.remove(defender)
        print(
            f"{attacker.name} наносит удар по {defender.name} на {damage} урона"
        )

    def fight(self):
        while len(self.persons) != 1:
            self.round_fight()
