"""hack_oop. Yandex.Praktikum. Game: "Battle of heroes"."""
from typing import List, Union, Dict
import random as rnd

CURRENT_LANG = 'eng'

ITEM_TYPES = ['ring', 'shield', 'mental_capacity', 'weapon']  # four types now
ITEMS_NAME = [['Charm', 'Superpower', 'Dexterity'],
              ['SteelWall', 'StoneBlock', 'RubberDuck'],
              ['Gain', 'SuperGain', 'SuperPuperGain'],
              ['MiniSword', 'BFG9000', 'M72 Gauss Rifle']]

PERSON_NAME: List[str] = ['Sulik', 'Vic', 'Cassidy', 'Myron', 'Davin',
                          'Miria', 'Lenny', 'Marcus', 'Robobrain',
                          'Goris', 'Cyberdog', 'K-9', 'Elder', 'Hakunin',
                          'First Citizen Lynette', 'Tandi', 'Harold',
                          'Enclave Soldier', 'Enclave Sergeant', 'ChoosenOne']

THING_FOR_BATTLE_MIN = 3
THING_FOR_BATTLE_MAX = 50
THING_DEF_PCNT_MAX = 10.0  # 10%
THING_DEF_PCNT_MIN = 1.0   # 1%
THING_ATTACK_MAX = 75.0
THING_ATTACK_MIN = 20.0
THING_HP_MIN = 100.0
THING_HP_MAX = 300.0

PERSON_HP_MAX = 1000
PERSON_HP_MIN = 300
PERSON_ATTACK_MAX = 100
PERSON_ATTACK_MIN = 20
PERSON_DEFENSE_MAX = 200
PERSON_DEFENSE_MIN = 50
PERSON_FOR_BATTLE = 10

MAX_GEN_ITEM = 100
ITEM_PERS_MAX = 4
ITEM_PERS_MIN = 1


class Thing():
    def __init__(self, item_type: str, item_name: str,
                 defense_percent: int, attack: int, hp_points: int):
        self.item_type: str = item_type
        self.item_name: str = item_name
        self.defense_percent: int = defense_percent
        self.attack: int = attack
        self.hp_points: int = hp_points


class Gen_thing():
    def __init__(self):
        self.thing_def_pcnt_max: int = THING_DEF_PCNT_MAX
        self.thing_def_pcnt_min: int = THING_DEF_PCNT_MIN
        self.thing_attack_max: int = THING_ATTACK_MAX
        self.thing_attack_min: int = THING_ATTACK_MIN
        self.thing_hp_min: int = THING_HP_MIN
        self.thing_hp_max: int = THING_HP_MAX

    def create_thing(self):
        item_type: int = rnd.randint(1, len(ITEM_TYPES)-1)
        item_name: int = rnd.randint(1, len(ITEMS_NAME[0])-1)

        cur_item_type: str = ITEM_TYPES[item_type]
        cur_item_name: str = ITEMS_NAME[item_type][item_name]

        defense_percent: int = int((rnd.random()
                                   * (THING_DEF_PCNT_MAX
                                   - THING_DEF_PCNT_MIN)
                                   + THING_DEF_PCNT_MIN))

        attack: int = int((rnd.random() * (THING_ATTACK_MAX
                          - THING_ATTACK_MIN) + THING_ATTACK_MIN))

        hp_points: int = int((rnd.random() * (THING_HP_MAX - THING_HP_MIN)
                             + THING_HP_MIN))

        return (Thing(cur_item_type, cur_item_name,
                defense_percent, attack, hp_points))


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
        self.attack: int = self.base_attack * 2


class Gen_person():
    def __init__(self):
        self.pers_hp_max: int = PERSON_HP_MAX
        self.pers_hp_min: int = PERSON_HP_MIN
        self.pers_attack_max: int = PERSON_ATTACK_MAX
        self.pers_attack_min: int = PERSON_ATTACK_MIN
        self.pers_defense_max: int = PERSON_DEFENSE_MAX
        self.pers_defense_min: int = PERSON_DEFENSE_MIN

    def create_person(self):
        name: str = PERSON_NAME[rnd.randint(1, 19)]
        hp: int = rnd.randint(self.pers_hp_min, self.pers_hp_max)
        attack: int = rnd.randint(self.pers_attack_min, self.pers_attack_max)
        defense: int = rnd.randint(self.pers_defense_min,
                                   self.pers_defense_max)

        choice: int = rnd.randint(1, 20)
        if choice > 10:
            return [Paladin(name, hp, attack, defense)]
        return [Warrior(name, hp, attack, defense)]


class Battle():
    def __init__(self, gen_things, gen_pers):
        self.item_list: List[Thing] = [gen_things.create_thing()
                                       for x in range(MAX_GEN_ITEM)]

        self.person_list: List[Union[Warrior, Paladin]]
        self.person_list = [gen_pers.create_person()
                            for x in range(PERSON_FOR_BATTLE)]

        count_things: int = rnd.randint(ITEM_PERS_MIN, ITEM_PERS_MAX)
        things_for_pers: List[Thing]
        things_for_pers = []
        for i in range(count_things):
            things_for_pers.append(self.item_list[rnd.randint(1,
                                   MAX_GEN_ITEM)])

        self.armed_pers_lst = [x.setThings(things_for_pers) for
                               x in range(PERSON_FOR_BATTLE)]

    def battle_turn(self):  # damage log
        pers_attaker_num = rnd.randint(1, len(self.person_list))
        while True:
            pers_defender_num = rnd.randint(1, len(self.person_list))
            if pers_attaker_num == pers_defender_num:
                continue
        pers_attaker = self.person_list[pers_attaker_num]
        pers_defender = self.person_list[pers_defender_num]

        attack = pers_attaker.full_attack
        turn_result = pers_defender.hp_substr(attack)
        if turn_result <= 0:
            self.armed_pers_lst = sorted(self.armed_pers_lst,
                                         key=self.sort_key, reverse=True)
            self.armed_pers_lst.listpop()

        result = {'attaker': pers_attaker, 'defender': pers_defender,
                  'res': turn_result}
        return result

    def sort_key(x):
        return x.full_hp

    def battle_status(self):  # leave persons
        return self.armed_pers_lst


class DictsInLang():
    """Contain dicts of game inventory in known languages"""
    def __init__(self, lang: str) -> None:
        self.curr_lang: str = lang
        self.eng_dict: Dict[str, str]
        self.eng_dict = {
                         'ring': 'Ring',
                         'shield': 'Shield',
                         'mental_capacity': '',
                         'weapon': 'Weapon',
                         'Charm': 'Charm',
                         'Superpower': 'Superpower',
                         'Dexterity': 'Dexterity',
                         'SteelWall': 'SteelWall',
                         'StoneBlock': 'StoneBlock',
                         'RubberDuck': 'RubberDuck',
                         'Gain': 'Gain',
                         'SuperGain': 'SuperGain',
                         'SuperPuperGain': 'SuperPuperGain',
                         'MiniSword': 'MiniSword',
                         'BFG9000': 'BFG9000',
                         'M72 Gauss Rifle': 'M72 Gauss Rifle'
                         }
        self.rus_dict: Dict[str, str]
        self.rus_dict = {
                         'ring': 'Кольцо',
                         'shield': 'Щит',
                         'mental_capacity': 'Особая способность',
                         'weapon': 'Оружие',
                         'Charm': 'Очарование',
                         'Superpower': 'Суперсила',
                         'Dexterity': 'Ловкость',
                         'SteelWall': 'Стальная Стена',
                         'StoneBlock': 'Каменная глыба',
                         'RubberDuck': 'Резиновая уточка',
                         'Gain': 'Усиление',
                         'SuperGain': 'Супер Усиление',
                         'SuperPuperGain': 'Супер-Пупер Усиление',
                         'MiniSword': 'маленький скромный мечик',
                         'BFG9000': 'BFG9000',
                         'M72 Gauss Rifle': 'Винтовка Гаусса M72'
                        }
        self.all_dict: Dict[str, Dict[str, str]]
        self.all_dict = {'eng': self.eng_dict, 'rus': self.rus_dict}

    def return_title(self, item: str) -> str:
        """Return title of game item in current Human's lang"""
        return self.all_dict[self.curr_lang][item]


def main():
    # game_dict: DictsInLang = DictsInLang(CURRENT_LANG)

    generator_persons = Gen_person()
    generator_things = Gen_thing()

    print('Стартует игра на выбывание')
    print('Участвуют: ', PERSON_NAME)

    print('Создаём Битву: ')
    battle = Battle(generator_things, generator_persons)
    print(Gen_thing.create_thing())

    print('В битве участвуют: ')
    print(battle.battle_status())


if __name__ == "__main__":
    main()
