'''Персонажи.'''

from things import Thing


class Person:
    '''Класс персонажа'''
    def __init__(self,
                 name: str,
                 number_of_lives: int,
                 base_attack: int,
                 base_defense_percentage: int):
        self.name = name
        self.number_of_lives = number_of_lives
        self.attack = base_attack
        self.defense_percentage = base_defense_percentage
        self.things = []

    def __str__(self):
        return (f'{self.name}: жизней - {self.number_of_lives}'
                f', атака - {self.attack}'
                f', % защиты - {self.defense_percentage}')

    def add_thing(self, thing: Thing):
        self.things.append(thing)
        self.number_of_lives += thing.number_of_lives
        self.attack += thing.attack
        self.defense_percentage += thing.defense_percentage
        self.defense_percentage = min(self.defense_percentage,
                                      100)

    def delete_thing(self, thing_num: int):
        if thing_num < len(self.things):
            thing = self.things.pop(thing_num)
            self.number_of_lives -= thing.number_of_lives
            self.attack -= thing.attack
            self.defense_percentage -= thing.defense_percentage

    def set_things(self, thinsg):
        for thing in thinsg:
            self.add_thing(thing)


class Paladin(Person):
    '''Класс персонажа Паладин.'''
    def __init__(self,
                 name: str,
                 number_of_lives: int,
                 base_attack: int,
                 base_defense_percentage: int):
        super().__init__(name,
                         number_of_lives,
                         base_attack,
                         base_defense_percentage)
        self.number_of_lives *= 2
        self.defense_percentage *= 2

    def __str__(self):
        return 'Паладин ' + super().__str__()


class Warrior(Person):
    '''Класс персонажа Воин'''
    def __init__(self,
                 name: str,
                 number_of_lives: int,
                 base_attack: int,
                 base_defense_percentage: int):
        super().__init__(name,
                         number_of_lives,
                         base_attack,
                         base_defense_percentage)
        self.attack *= 2

    def __str__(self):
        return 'Воин ' + super().__str__()
