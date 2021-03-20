"""hack_oop. Yandex.Praktikum. Game: "Battle of heroes"."""

import game_content
import game_algorithms
from game_languages import DictsInLang
CURRENT_Lang = 'eng'


def main():
    game_dict: DictsInLang = DictsInLang(CURRENT_Lang)

    print('Стартует игра на выбывание')
    print('Участвуют: ', PERSON_NAME)

    
if __name__ == "__main__":
    main()
