from typing import List

from rich.console import Console

console = Console()


class Thing:
    """Different things (closes, weapons etc.) with characteristics."""

    def __init__(
        self,
        name: str,
        per_proc: float = 0,
        thing_attack: float = 0,
        hp: float = 0,
    ) -> None:
        self.name = name
        self.per_proc = per_proc
        self.attack = thing_attack
        self.hp = hp

    def __str__(self):
        return self.name


class Person:
    "Base class for player."

    def __init__(
        self, name, hp: float, base_attack: float, base_protect: float
    ) -> None:
        self.name = name
        self.base_hp = hp
        self.base_attack = base_attack
        self.base_deffend = base_protect
        self.inventory = {}
        self.current_attack = base_attack
        self.current_protect = base_protect
        self.current_hp = hp

    def setThings(self, things: List[Thing]) -> None:
        """Set all things in list on character. Like a backpack.
        Change person characteristic immideatly.
        """
        for thing in things:
            self.inventory[thing.name] = thing
            self.current_hp += thing.hp
            self.current_attack += thing.attack
            self.current_protect += thing.per_proc
            console.print(f"На персонажа {self.name} надели {thing.name}")

    def showThings(self) -> str:
        "Show all things seted on person"
        list_thing = [thing for thing in self.inventory]
        console.print(list_thing)

    def calculate_hp_attack(self, attacker: "Person") -> float:
        """Calculate damage from attacker and decrease hp on it."""
        amount_damage = (
            attacker.current_attack
            - attacker.current_attack * self.current_protect
        )
        self.current_hp -= amount_damage
        self.current_hp = round(self.current_hp, 2)
        if self.current_hp <= 0:
            self.current_hp = 0
        return round(amount_damage, 2)


class Paladin(Person):
    "Paladin calss. Has a 2x hp and 2x deffend."

    def __init__(
        self, name, hp: float, base_attack: float, base_protect: float
    ) -> None:
        super().__init__(name, hp, base_attack, base_protect)
        self.base_hp *= 2
        self.base_deffend *= 2


class Warrior(Person):
    "Warrior class has a 2x attack."

    def __init__(
        self, name, hp: float, base_attack: float, base_deffend: float
    ) -> None:
        super().__init__(name, hp, base_attack, base_deffend)
        self.base_attack *= 2
