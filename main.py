class Thing:
    """Class for creating things for game characters."""
    def __init__(self, thing_name: str,
                 thing_protection: float,
                 thing_attack: int,
                 thing_health: int) -> None:
        self.thing_name = thing_name
        self.thing_protection = thing_protection
        self.thing_attack = thing_attack
        self.thing_health = thing_health

    def __str__(self) -> str:
        return self.thing_name


class Person:
    """The class that creates the characters in the game."""
    def __init__(self, person_name: str,
                 person_protection: float,
                 person_attack: int,
                 person_health: int) -> None:
        self.person_name = person_name
        self.person_protection = person_protection
        self.person_attack = person_attack
        self.person_health = person_health

    def __str__(self) -> str:
        return self.person_name

    def set_things(self, things: list) -> None:
        """Dress up the game character with items from the list."""
        for thing in things:
            self.person_protection += thing.thing_protection
            self.person_protection = round(self.person_protection, 2)
            self.person_attack += thing.thing_attack
            self.person_health += thing.thing_health

    def damage_to_health(self, attack_damage: int) -> None:
        """Calculates damage when attacking by another character."""
        self.person_health -= attack_damage - attack_damage * self.person_protection


class Paladin(Person):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.person_health *= 2
        self.person_protection *= 2


class Warrior(Person):
    """The class that creates warriors."""
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.person_attack *= 2
