'''Предметы.'''


class Thing:
    '''Класс Предмет.'''
    def __init__(self,
                 name: str,
                 defense_percentage: int,
                 attack: int,
                 number_of_lives: int):
        self.name = name
        self.defense_percentage = defense_percentage
        self.attack = attack
        self.number_of_lives = number_of_lives

    def __str__(self):
        return (f'{self.name}'
                f':\tзащита = {self.defense_percentage}'
                f'\tатака = {self.attack}'
                f'\tжизней = {self.number_of_lives}')

    def __eq__(self, other):
        if isinstance(other, Thing):
            return (self.defense_percentage == other.defense_percentage and
                    self.attack == other.attack and
                    self.number_of_lives == other.number_of_lives)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Thing):
            if self.defense_percentage > other.defense_percentage:
                return True
            if (self.defense_percentage == other.defense_percentage and
               self.attack > other.attack):
                return True
            if (self.defense_percentage == other.defense_percentage and
               self.attack == other.attack and
               self.number_of_lives > other.number_of_lives):
                return True
            return False
        return NotImplemented
