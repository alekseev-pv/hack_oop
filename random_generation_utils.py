import random
from typing import List, Tuple

from things import Things

THING_NAMES = ['кольцо',
               'пояс',
               'ушки',
               'хвостик',
               'когти',
               'рог единорога',
               'лапки']

PERSON_NAMES: List[str] = [
    'Пёсик Гав',
    'Котик Василий',
    'Пёсик Чимс',
    'Котик Матроскин',
    'Пёсик Доге',
    'Котик Том',
    'Пёсик Шарик',
    'Котик Гарфилд',
    'Пёсик Хатико',
    'Котик Чешир',
    'Пёсик Пиклз',
    'Котик Санрио',
    'Пёсик Белка',
    'Котик Царапина',
    'Пёсик Стрелка',
    'Котик Тигра',
    'Пёсик Макс',
    'Котик Симба',
    'Пёсик Лаки',
    'Котик Учёный'
]

PERSONS_TYPES = ['Paladin', 'Warrior', 'CatDog']


class RandomGenerationUtils:

    @staticmethod
    def get_random_thing() -> Things:
        """
        Сгенерировать случайную вещь

        name - случайно из списка имён
        per_protection - максимум 0,1
        attack - случайно от 1 до 20
        life - случайно от 1 до 20
        """
        name = THING_NAMES[random.randint(0, len(THING_NAMES) - 1)]
        per_protection = round(random.uniform(0, 0.1), 2)
        attack = random.randint(1, 20)
        life = random.randint(1, 20)
        return Things(name=name, per_protection=per_protection,
                      attack=attack, life=life)

    @staticmethod
    def get_random_person_params() -> Tuple[int, int, float]:
        """
        Сгенерировать параметры для персонажа

        life_counter - случайно от 20 до 100
        base_attack - случайно от 5 до 40
        base_protection - случайно от 0.1 до 0.25
        """
        life_counter = random.randint(20, 100)
        base_attack = random.randint(5, 40)
        base_protection = round(random.uniform(0.1, 0.25), 2)
        return life_counter, base_attack, base_protection

    @staticmethod
    def get_random_person_names_list(number) -> List[str]:
        """
        Получить список уникальных имён персонажей - отобрать из списка имён
        """
        return random.sample(PERSON_NAMES, number)

    @staticmethod
    def get_random_person_type():
        return PERSONS_TYPES[random.randint(0, len(PERSONS_TYPES) - 1)]
