class Thing:
    """Шмотки для персонажей с характеристиками."""

    def __init__(
        self,
        name: str,
        per_proc: float = None,
        attack: float = None,
        life: float = None,
    ) -> None:
        self.name = name
        self.per_proc = per_proc
        self.attack = attack
        self.life = life


class Person:
    def __init__(
        self, hp: float, base_attack: float, base_deffend: float
    ) -> None:
        self.hp = hp
        self.base_attack = base_attack
        self.base_deffend = base_deffend

    def setThings(self, things):
        pass

    def calculate_hp(self):
        pass


class Paladin(Person):
    pass


class Warrior(Person):
    pass
