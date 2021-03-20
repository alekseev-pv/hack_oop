from typing import List, Optional


class Thing():
    def __init__(self, name: str, hp: float = 0,
                 damage: float = 0, protection: float = 0):
        self.name = name
        self.protection = protection
        self.damage = damage
        self.hp = hp


class Person():
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


class Paladin(Person):
    def __init__(self, name: str, hp: float, damage: float, protection: float):
        super().__init__(name, hp * 2, damage, protection * 2)


class Warrior(Person):
    def __init__(self, name: str, hp: float, damage: float, protection: float):
        super().__init__(name, hp, damage * 2, protection)
