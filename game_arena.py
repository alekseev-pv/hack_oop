import random


class Thing:
    NAMES_THING = ['шлем', 'нагрудник', 'наплечники',
                   'перчатки', 'пояс', 'поножи',
                   'сапоги', 'меч', 'топор', 'щит']

    def __init__(self):
        self.name = random.choice(self.NAMES_THING)
        self.defense = round(random.uniform(0, 10)/100, 2)
        self.attack = random.randint(0, 10)
        self.hp = random.randint(0, 30)


class Person:
    NAMES_PERSON = ['Халвадор', 'Линетта', 'Каваи', 'Декрин',
                    'Аромет', 'Сукмот', 'Рохиеса', 'Форина',
                    'Миркан', 'Кристол', 'Бутрон', 'Трин',
                    'Миркана', 'Ворстол', 'Битра', 'Амаури'
                    'Джелли', 'Фиокир', 'Трикон', 'Янкир']

    def __init__(self):
        self.name = random.choice(self.NAMES_PERSON)
        self.hp = 100
        self.attack = 5
        self.defense = 0.1

    def set_things(self, things):
        for thing in things:
            self.hp += thing.hp
            self.attack += thing.attack
            self.defense += thing.defense

    @staticmethod
    def attacking(attacker, defender):
        return defender.hp - (attacker.attack - attacker.attack*defender.defense)


class Paladin(Person):
    def __init__(self):
        super().__init__()
        self.defense *= 2
        self.hp *= 2


class Warrior(Person):
    def __init__(self):
        super().__init__()
        self.attack *= 2


class Arena:
    pass
