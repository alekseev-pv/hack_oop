# Классы для программы

class Thing():
    def __init__(self, name='Ninja', protection=0, power=0, healpoints=0):
        self.name = name
        self.protection = protection
        self.power = power
        self.healpoints = healpoints
    
    def __str__(self) -> str:
        return (f'Вещь: {self.name}, здоровье: {self.healpoints}, '
            f'сила: {self.power}, защита: {self.protection}')
            

class Person():
    def __init__(self, person_name, base_healpoints=100,
        base_power=10, base_protection=0):
        self.person_name = person_name
        self.base_healpoints = base_healpoints
        self.base_power = base_power
        self.base_protection = base_protection
        self.healpoints = self.base_healpoints
        self.power = self.base_power
        self.protection = self.base_protection
        self.things = []

    def set_things(self, thing):
        self.healpoints = self.healpoints + thing.healpoints
        self.power = self.power + thing.power
        self.protection = self.protection + thing.protection
        pass

    def get_attacked(self, Person):
        attack_damage = Person.power - Person.power * self.protection
        self.healpoints = self.healpoints - attack_damage
        print(
            f'`{Person.person_name} наносит удар по '
            f'{self.person_name} на {attack_damage} урона`'
        )

    def show_things(self):
        for thing in self.things:
            if thing.name:
                print(thing.name)

    def is_alive(self):
        if self.healpoints > 0:
            return True
        return False

    def __str__(self) -> str:
        reply = (
            f'\nУчастник {self.person_name} {type(self).__name__} '
            f'имеет Здоровье = {self.healpoints} '
            f'Силу атаки = {self.power} и Защиту = {self.protection} '
        )
        for thing in self.things:
            reply += '\n' + str(thing)
        return reply


class Paladin(Person):
    def __init__(self, **kwargs):
        super(Paladin, self).__init__(**kwargs)
        self.healpoints = self.base_healpoints * 2
        self.protection = self.base_protection * 2


class Warrior(Person):
    def __init__(self, **kwargs):
        super(Warrior, self).__init__(**kwargs)
        self.power = self.base_power * 2
