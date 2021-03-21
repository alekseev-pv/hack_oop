"""Пример использования.
>>>Thing.create(20)
>>>Person.create_person()
>>>Arena.fight()
"""

import random


class Thing:
    """Класс вещей.

    Attributes
    ----------
    thing_objects_list : list
        хранит в себе все объекты класса вещей.

    Methods
    -------
    create()
        создаёт count объектов класса.
    """

    thing_objects_list = []

    def __init__(self, name, protect=0, attack=0, heals_point=0):
        self.name = name
        self.protect = protect
        self.attack = attack
        self.heals_point = heals_point

    @staticmethod
    def create(count):
        """Создает count объектов класса с рандомными значениями атрибутов.

        Готовый список объектов (Thing.thing_objects_list) передает в класс
        Person метод setThings()
        """
        for i in range(1, count + 1):
            name_list = ['Ring', 'Sword', 'Mace', 'shield', 'hauberk']
            name = random.choice(name_list)
            protect = round(random.uniform(0.01, 0.05), 2)
            attack = random.randint(5, 10)
            heals_point = random.randint(1, 10)
            Thing.thing_objects_list.append(Thing(name,
                                            protect, attack, heals_point))
        Person.setThings(Thing.thing_objects_list)


class Person:
    """Класс для управления и инициализации классов Paladin, Warrior

    Methods
    -------
    create_person()
        Рандомно создаёт 10 объектов (Paladin или Warrior) присваивая
        им рандомное имя из списка list_of_fighters.
    setThings()
        Получает в качестве аргумента список всех объектов класса Thing,
        создаёт атрибут класса с этим списком.
    dispanse_things()
        Раздает каждому бойцу рандомно от 1 до 4 вещи.
    damage()
        Вычитает жизни на основе входной атаки.
    """

    def __init__(self, name):
        self.name = name
        self.heals_point = 100
        self.attack = 10
        self.protect = 0.05

    @staticmethod
    def create_persons():
        """
        Рандомно создаёт 10 объектов (Paladin и Warrior) присваивая
        им рандомное имя из списка list_of_fighters.
        """
        list_of_fighters = []
        name = ['John', 'Harry', 'Oliver', 'Jack', 'Charlie', 'Thomas',
                'Jacob', 'Alfie', 'Riley', 'William', 'James', 'Daniel',
                'Ethan', 'Noah', 'Mason', 'Lewis',
                'Logan', 'Alex', 'Ava', 'Mia']
        for i in range(1, 11):
            random_name_first = random.choice(name)
            name.remove(random_name_first)
            random_name_second = random.choice(name)
            name.remove(random_name_second)
            paladin_or_warrior = [Paladin(random_name_first),
                                  Warrior(random_name_second)]
            list_of_fighters.append(random.choice(paladin_or_warrior))
        Person.list_of_fighters = list_of_fighters

    @staticmethod
    def setThings(thing):
        """
        Получает в качестве аргумента список всех объектов класса Thing,
        создаёт атрибут класса с этим списком.
        """
        Person.thing = thing

    def dispanse_things(self):
        """Раздает каждому бойцу рандомно от 1 до 4 вещи."""
        index = len(Person.thing) - 1
        if len(Person.thing) >= 4:
            span = 4
        elif len(Person.thing) == 3:
            span = 3
        elif len(Person.thing) == 2:
            span = 2
        else:
            span = 1

        if len(Person.thing) >= 1:

            for i in range(1, random.randint(1, span + 1)):
                thing_object = Person.thing.pop(random.randint(0, index))
                index -= 1
                self.heals_point += thing_object.heals_point
                self.attack += thing_object.attack
                self.protect += thing_object.protect

    @staticmethod
    def damage(attacker, defender):
        """Вычитает жизни на основе входной атаки."""
        damage = (attacker.attack - attacker.attack * defender.protect)
        defender.heals_point -= damage
        print(f'{attacker.name} наносит удар по '
              f'{defender.name} на {damage} урона')


class Paladin(Person):
    """Класс создания бойца типа Paladin
    Основные свои свойства и функционал наследует от класса Person.
    """

    def __str__(self):
        return self.name

    def __init__(self, name):
        Person.__init__(self, name)
        self.heals_point = self.heals_point * 2
        self.protect = self.protect * 2
        self.dispanse_things()


class Warrior(Person):
    """Класс создания бойца типа Warrior
    Основные свои свойства и функционал наследует от класса Person.
    """

    def __str__(self):
        return self.name

    def __init__(self, name):
        Person.__init__(self, name)
        self.attack = self.attack * 2
        self.dispanse_things()


class Arena:
    """Арена для битвы
    Выбирается рандомная пара Нападающий и Защищающийся
    В живых останется один, он и получит приз!
    """
    @staticmethod
    def fight():
        list_of_fighters = Person.list_of_fighters
        while len(list_of_fighters) != 1:
            attacker = random.choice(list_of_fighters)
            index = list_of_fighters.index(attacker)
            pop = list_of_fighters.pop(index)
            defender = random.choice(list_of_fighters)
            list_of_fighters.append(pop)
            Person.damage(attacker, defender)
            if defender.heals_point <= 0:
                list_of_fighters.remove(defender)
            if len(list_of_fighters) == 1:
                print(f'ПОБЕДИТЕЛЬ - {list_of_fighters[0]}, сектор приз '
                      f'на барабане, он выиграл ААААААААВТОМОБИЛЬ!')
