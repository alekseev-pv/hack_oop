import random


class Thing:
    def __init__(self, name, defense, attack, hp):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.hp = hp


class Person:
    def __init__(self, name):
        self.name = name
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
    NAMES_THING = ['шлем', 'нагрудник', 'наплечники',
                   'перчатки', 'пояс', 'поножи',
                   'сапоги', 'меч', 'топор', 'щит']
    NAMES_PERSON = ['Халвадор', 'Линетта', 'Каваи', 'Декрин',
                    'Аромет', 'Сукмот', 'Рохиеса', 'Форина',
                    'Миркан', 'Кристол', 'Бутрон', 'Трин',
                    'Миркана', 'Ворстол', 'Битра', 'Амаури'
                    'Джелли', 'Фиокир', 'Трикон', 'Янкир']

    def creat_things(self):
        things = []
        thing = Thing(
            name=random.choice(self.NAMES_THING),
            defense=round(random.uniform(0, 10)/100, 2),
            attack=random.randint(0, 10),
            hp=random.randint(0, 30))
        count = 80
        if len(things) < count:
            things.append(thing)
            count -= count
        things.sort()

    def creat_characters(self):
        characters = []
        count = random.randint(1,2)

