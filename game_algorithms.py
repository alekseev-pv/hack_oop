"""Game: "Battle of heroes" Module game_algorithms."""
import random as rnd
from typing import List, Union
from game_content import Thing
import game_content
import game_algorithms
from game_languages import DictsInLang

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


# создание вещей генератор
class gen_thing():
    def __init__(self):
        # взять параметры генерации вещей
        self.thing_def_pcnt_max: int = THING_DEF_PCNT_MAX
        self.thing_def_pcnt_min: int = THING_DEF_PCNT_MIN
        self.thing_attack_max: int = THING_ATTACK_MAX
        self.thing_attack_min: int = THING_ATTACK_MIN
        self.thing_hp_min: int = THING_HP_MIN
        self.thing_hp_max: int = THING_HP_MAX

    def create_thing(self) -> Thing:
        item_type: int = rnd.randint(1, len(ITEM_TYPES))
        item_name: int = rnd.randint(1, len(ITEMS_NAME[item_type]))
        cur_item_type: str = ITEM_TYPES[item_type-1]
        cur_item_name: str = ITEMS_NAME[cur_item_type][item_name-1]

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


class gen_person():
    def __init__(self):
        self.pers_hp_max: int = PERSON_HP_MAX
        self.pers_hp_min: int = PERSON_HP_MIN
        self.pers_attack_max: int = PERSON_ATTACK_MAX
        self.pers_attack_min: int = PERSON_ATTACK_MIN
        self.pers_defense_max: int = PERSON_DEFENSE_MAX
        self.pers_defense_min: int = PERSON_DEFENSE_MIN

    def create_person(self): 
        name: str = PERSON_NAME[rnd.randint(1, 20)] 
        hp: int = rnd.randint(self.pers_hp_min, self.pers_hp_max)
        attack: int = rnd.randint(self.pers_attack_min, self.pers_attack_max)
        defense: int = rnd.randint(self.pers_defense_min,
                                   self.pers_defense_max)

        choice: int = rnd.randint(1, 20)
        if choice > 10:
            return [Paladin(name, hp, attack, defense)]
        return [Warior(name, hp, attack, defense)]
        

class Battle():
    def __init__(self):
        self.item_list: List[Thing] = [gen_thing.create_thing()
                                       for x in range(MAX_GEN_ITEM)]

        self.person_list: List[Union[Warior, Paladin]]
        self.person_list = [gen_person.create_person()
                            for x in range(PERSON_FOR_BATTLE)]

        count_things: int = rnd.randint(ITEM_PERS_MIN, ITEM_PERS_MAX)
        things_for_pers: List[Thing] 
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



