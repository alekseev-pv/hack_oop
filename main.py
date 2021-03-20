from typing import List, Optional


class Thing:
    """Вещи модифицирующие характеристики персонажа"""

    def __init__(
        self,
        name: str,
        hit_points: float,
        protection: float,
        attack_damage: float,
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

        bonus_hit_point = sum([thing.protection for thing in self.things])
        self.final_protection = self.protection + bonus_hit_point

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
