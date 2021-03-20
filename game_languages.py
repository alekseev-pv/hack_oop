"""Game: "Battle of heroes". Module game_languages.

Known languages is Russian and English.
"""
from typing import Dict


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
