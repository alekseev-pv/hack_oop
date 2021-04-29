import random
from typing import List, Optional, Tuple
from dataclasses import dataclass
from package.errors import InventoryOverflowError, DropThingError

from colorama import Back, Fore, Style


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

    def __str__(self):
        return f"{self.name}"


class Inventory:
    def __init__(self, size: int):
        self.size = size
        self.things: List[Thing] = []
        self.counter = 0

    def add_thing(self, thing: Thing) -> bool:
        """При переполнении инвентаря возвращает False"""
        if len(self.things) >= self.size:
            return False
        self.things.append(thing)
        return True

    def drop_thing(self, thing: Thing = None, index: int = None):
        if thing is None and index is None:
            raise DropThingError
        if thing is not None:
            self.things.remove(thing)
        else:
            del self.things[index]

    @property
    def number_empty_slots(self):
        return self.size - len(self.things) - 1

    def set_things(self, things: List[Thing]):
        if len(self.things) > self.size:
            raise InventoryOverflowError
        self.things = [thing for thing in things]

    def remove_thing(self, index):
        self.things.pop(index)

    def __str__(self) -> str:
        names_of_thing = [thing.name for thing in self.things]
        return ", ".join(names_of_thing)

    def __len__(self) -> int:
        return len(self.things)

    def __getitem__(self, key: int) -> Thing:
        return self.things[key]

    def __setitem__(self, key: int, thing: Thing) -> None:
        self.things[key] = thing

    def __delitem__(self, key: int) -> None:
        del self.things[key]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.things):
            self.counter += 1
            return self.things[self.counter - 1]
        else:
            raise StopIteration

    def append(self, thing: Thing) -> None:
        """Выбрасывает ошибку при переполнении инвертаря"""
        if len(self.things) >= self.size:
            raise InventoryOverflowError
        self.things.append(thing)

    def head(self) -> Thing:
        return self.things[0]

    def tail(self) -> List[Thing]:
        return self.things[1:]

    def init(self) -> List[Thing]:
        return self.things[:-1]

    def last(self) -> List[Thing]:
        return self.things[-1]

    def drop(self, n) -> List[Thing]:
        return self.things[n:]

    def take(self, n) -> List[Thing]:
        return self.things[:n]


@dataclass
class AttackReport:
    attacker: object
    defender: object
    damag_sent: float
    damage_taken: float


class DefenderMixin:
    def __init__(self):
        self.hit_points: float
        self.current_hit_points: float
        self.final_hit_points: float

        self.protection: float
        self.final_protection: float

    def take_damage(self, damage: float) -> float:
        final_damage = damage - damage * self.final_protection
        final_damage = round(final_damage, 2)
        self.current_hit_points -= final_damage
        return final_damage

    def is_alive(self) -> bool:
        if self.current_hit_points <= 0:
            return False
        return True


class AttackerMixin:
    def __init__(self):
        self.attack_damage: float
        self.final_attack_damage: float

    def attack(self, defender: DefenderMixin) -> AttackReport:
        taken_damage = defender.take_damage(self.final_attack_damage)
        return AttackReport(
            attacker=self,
            defender=defender,
            damag_sent=self.final_attack_damage,
            damage_taken=taken_damage,
        )


class Person(DefenderMixin, AttackerMixin):
    def __init__(
        self,
        name: str,
        hit_points: float,
        protection: float,
        attack_damage: float,
        size_inventory: int = 4,
    ):
        self.name = name

        self.hit_points = hit_points
        self.current_hit_points = hit_points
        self.final_hit_points = hit_points

        self.protection = protection
        self.final_protection = protection

        self.attack_damage = attack_damage
        self.final_attack_damage = attack_damage

        self.inventory = Inventory(size_inventory)

    def _update_protection(self):
        bonus_protection = sum([thing.protection for thing in self.inventory])
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

    def take_thing(self, thing: Thing) -> bool:
        """Возвращает False в случае перполнения инвентаря"""
        if self.inventory.number_empty_slots < 1:
            return False
        self.inventory.append(thing)
        self.update_characteristics()
        return True

    def drop_thing(self, thing: Thing = None, index: int = None):
        self.inventory.drop_thing(thing=thing, index=index)
        self.update_characteristics()

    def set_inventory(self, things: List[Thing]):
        self.inventory.set_things(things)
        self.update_characteristics()

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


CLASSES_PESRONS: Tuple[Paladin, Warrior] = (Paladin, Warrior)


class Player:
    classes_persons = CLASSES_PESRONS

    def __init__(self, name: str):
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

        class_person: Person = self._choose_class()
        name = input("Введите имя персонажа\n")
        hit_point = int(input("Введите количество очков здоровья\n"))
        protection = int(input("Введите количество % бронки\n")) / 100
        attack_damage = int(input("Введите количество очков силы\n"))

        person = class_person(name, hit_point, protection, attack_damage)

        self.set_person(person)

    def take_thing(self, thing: Thing) -> None:
        if self.person.take_thing(thing):
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

    def show_fight_report(self, attack_report=AttackReport):
        damage_taken = attack_report.damage_taken

        col_attacker_name = (
            f"{Fore.YELLOW}{attack_report.attacker.name}{Style.RESET_ALL}"
        )
        col_kick = f"{Fore.RED}удар{Style.RESET_ALL}"
        col_defender_name = (
            f"{Fore.YELLOW}{attack_report.defender.name}{Style.RESET_ALL}"
        )
        col_damage = f"{Fore.RED}{damage_taken}{Style.RESET_ALL}"
        print(
            f"{col_attacker_name} наносит {col_kick} "
            f"по  {col_defender_name} на {col_damage} урона"
        )

    def show_die_report(self, attacker: Person, defender: Person):
        col_defender_name = f"{Fore.YELLOW}{defender.name}{Style.RESET_ALL}"
        col_attacker_name = f"{Fore.YELLOW}{attacker.name}{Style.RESET_ALL}"
        col_die = f"{Back.RED}погиб{Style.RESET_ALL}"
        print(f"{col_defender_name} {col_die} от рук {col_attacker_name}")

    def round_fight(self):
        couple_fighter = random.sample(self.persons, k=2)
        attacker: Person = couple_fighter[0]
        defender: Person = couple_fighter[1]
        attack_report = attacker.attack(defender)
        self.show_fight_report(attack_report)

        if not defender.is_alive():
            self.persons.remove(defender)
            self.show_die_report(attacker, defender)

    def fight(self) -> Person:
        """возвращает победителя"""
        while len(self.persons) != 1:
            self.round_fight()
        return self.persons[0]
