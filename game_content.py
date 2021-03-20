"""Game: 'Battle of heroes'. Module game_content."""
from typing import List
# import game_languages

# ITEM_TYPES: List[str]
# ITEMS_NAME: Dict[str, Tuple[]]
ITEM_TYPES = ['ring', 'shield', 'mental_capacity', 'weapon']  # four types now
ITEMS_NAME = {'ring': ('Charm', 'Superpower', 'Dexterity'),
              'shield': ('SteelWall', 'StoneBlock', 'RubberDuck'),
              'mental_capacity': ('Gain', 'SuperGain', 'SuperPuperGain'),
              'weapon': ('MiniSword', 'BFG9000', 'M72 Gauss Rifle')
              }
PERSON_NAME: List[str] = ['Sulik', 'Vic', 'Cassidy', 'Myron', 'Davin',
                          'Miria', 'Lenny', 'Marcus', 'Robobrain',
                          'Goris', 'Cyberdog', 'K-9', 'Elder', 'Hakunin',
                          'First Citizen Lynette', 'Tandi', 'Harold',
                          'Enclave Soldier', 'Enclave Sergeant', 'ChoosenOne']

class Nicknames():
    pass


class Thing():
    def __init__(self, item_type: str, item_name: str,
                 defense_percent: int, attack: int, hp_points: int):
        self.item_type: str = item_type
        self.item_name: str = item_name
        self.defense_percent: int = defense_percent
        self.attack: int = attack
        self.hp_points: int = hp_points


class Person():
    def __init__(self, name: str, hp: int, attack: int, pcnt_defense: int):
        self.pers_name: str = name
        self.pers_hp: int = hp
        self.base_attack: int = attack
        self.base_percent_defense: int = pcnt_defense

    def setThings(self, things: List[Thing]):
        self.add_def_pcnt: int = sum(x.defense_percent for x in things)
        self.add_attack: int = sum(x.attack for x in things)
        self.add_hp_points: int = sum(x.hp_points for x in things)

        self.full_hp: int = self.pers_hp + self.add_hp_points
        self.finalProtection: int = (self.base_percent_defense
                                     + self.add_def_pcnt)
        self.full_attack: int = self.base_attack + self.add_attack

    def hp_substr(self, attack_damage) -> int:
        turn_damage: float = (self.full_hp - attack_damage
                              + attack_damage * self.finalProtection / 100.0)
        self.full_hp -= round(turn_damage)
        return self.full_hp


class Paladin(Person):
    def __init__(self, name: str, hp: int, attack: int, pcnt_defense: int):
        super().__init__(name, hp, attack, pcnt_defense)
        self.pers_hp: int = self.pers_hp * 2
        self.base_percent_defense: int = self.base_percent_defense * 2


class Warrior(Person):
    def __init__(self, name: str, hp: int, attack: int, pcnt_defense: int):
        super().__init__(name, hp, attack, pcnt_defense)
        self.attack: int = self.attack * 2
