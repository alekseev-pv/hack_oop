from typing import List, Tuple, Optional, Dict
import random


class NameGenerator:
    def __init__(self, nouns: List[Dict], subjects: List[str]):
        self.nouns = nouns
        self.subjects = subjects

    def get_names(self, number_names):
        nouns = random.choices(self.nouns, k=number_names)
        subjects = random.choices(self.subjects, k=number_names)

        return [f"{nouns[i]} {subjects[i]}" for i in range(number_names)]


class Thing:
    """Вещи модифицирующие характеристики персонажа"""

    def __init__(
        self,
        name: str,
        multiplier_hit_points: float = 0,
        protection: float = 0,
        attack_damage: float = 0,
    ):
        self.name = name
        self.multiplier_hit_points = multiplier_hit_points
        self.protection = protection
        self.attack_damage = attack_damage


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


class InventoryError(Exception):
    pass


class InventoryOverflowError(InventoryError):
    pass


class Inventory:
    def __init__(self, size: int):
        self.size = size
        self.things: List[Thing] = []

    def add_thing(self, thing: Thing) -> bool:
        """При переполнении инвентаря возвращает False"""
        if len(self.things) >= self.size:
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

        self.inventory = Inventory(self.MAX_SIZE_INVENTORY)

    def _update_protection(self):
        bonus_protection = sum(
            [thing.protection for thing in self.inventory.things]
        )
        self.final_protection = self.protection + bonus_protection

    def _update_attack_damage(self):
        bonus_attack_damage = sum(
            [thing.attack_damage for thing in self.inventory.things]
        )
        self.final_attack_damage = self.attack_damage + bonus_attack_damage

    def _update_hit_points(self):
        sum_multiplier_hit_points = sum(
            [thing.multiplier_hit_points for thing in self.inventory.things]
        )
        # для расчёта неполного здоровья при поднятии/снятии предмета
        # для коррекции текущего здоровья, расчитываеся разница
        # между новым итоговым и старым итоговым
        # нужено более элегантное решение

        new_final_hit_points = (
            self.hit_points + self.hit_points * sum_multiplier_hit_points
        )
        if self.final_hit_points != new_final_hit_points:
            correction_factor = new_final_hit_points / self.final_hit_points
            self.current_hit_points = (
                self.current_hit_points * correction_factor
            )
            self.final_hit_points = new_final_hit_points

    def update_characteristics(self):
        self._update_protection()
        self._update_attack_damage()
        self._update_hit_points()

    def set_inventory(self, things: List[Thing]):
        self.inventory.set_things(things)
        self.update_characteristics()

    def add_thing(self, thing: Thing) -> bool:
        """При переполнении инвентаря возвращает False"""
        if not self.inventory.add_thing(thing):
            return False
        self.update_characteristics()
        return True

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
    MAX_PROTECTION = 0.2
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
    classes_persons = [Paladin, Warrior]

    def __init__(
        self,
        name: str,
    ):
        self.name = name
        self.person: Optional[Person] = None

    def set_person(self, person: Person):
        self.person = person
        print(f"Игрок выбрал {person}")

    def _choose_class(self) -> Person:
        print("Выберете класс")
        for i, cl in enumerate(self.classes_persons):
            print(f"{i}) {cl.__name__}")
        try:
            number_class = int(input("Введите номер класса\n"))
        except BaseException:
            print("некорректный ввод, попробуйте ещё раз")
            return self._choose_class()

        if 0 <= number_class < len(self.classes_persons):
            return self.classes_persons[number_class]
        else:
            print("некорректный ввод, попробуйте ещё раз")
            return self._choose_class()

    def create_person(self):

        class_person = self._choose_class()
        name = input("Введите имя персонажа\n")
        hit_point = int(input("Введите количество очков здоровья\n"))
        protection = int(input("Введите количество % бронки\n")) / 100
        attack_damage = int(input("Введите количество очков силы\n"))

        person = class_person(name, hit_point, protection, attack_damage)

        self.set_person(person)

    def take_thing(self, thing: Thing):
        if self.person.add_thing(thing):
            print(f"{self.person} взял {thing.name}")
        else:
            print(f"У {self.person} переполнился инвентарь")


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

    def add_player(self, player: Player):
        self.persons.append(player.person)

    def round_fight(self):
        couple_fighter = random.sample(self.persons, k=2)
        attacker: Person = couple_fighter[0]
        defender: Person = couple_fighter[1]
        damage = defender.reduce_hit_points(attacker.final_attack_damage)
        print(
            f"{attacker.name} наносит удар "
            f"по {defender.name} на {damage} урона"
        )

        if defender.current_hit_points <= 0:
            self.persons.remove(defender)
            print(f"{defender.name} погиб от рук {attacker.name} ")

    def fight(self) -> Person:
        """возвращает победителя"""
        while len(self.persons) != 1:
            self.round_fight()
        return self.persons[0]
