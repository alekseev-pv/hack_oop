"""
Игра арена

Игра, основанная по мотивам 'The Elder Scrolls: Arena' 1994г.
"""


class Person():
    def __init__(self, name) -> None:
        self.name = name
        self.hp: int = 10
        self.attack: int = 1
        self.protect: float = 0.01
        print('Создан персонаж по имени {0} с кол-ом здоровья {1}, атакой: {2} и защитой {3}%'.format(self.name, self.hp, self.attack, int(self.protect*100)))


class Thing():
    pass


class Paladin(Person):
    pass


class Warrior(Person):
    pass


first_hero = Person("Hero")