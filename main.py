from random import randint, choice, randrange
from colorama import Fore


class Things:
    """Class for items"""

    NAMES = [
        'ring', 'helm', 'boots', 'armor', 'gloves', 'cloak',
        'sword', 'club', 'spear', 'pants', 'shirt', 'necklace',
        'earring', 'golden tooth', 'bow', 'dagger', 'elder scroll'
        'crown', 'Holy Grail', 'staff', 'magic wand', 'scroll of spell',
        'bottle'
    ]

    items = []
    items_in_use = []

    def __init__(self, name, protection, attack, hp):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.hp = hp
        self.items.append(self)

    @staticmethod
    def generate_items():
        for _ in range(randint(10, 40)):
            attributs = {
                'protection': 0,
                'attack': 0,
                'hp': 0
            }
            attribut = choice(['protection', 'attack', 'hp'])
            if attribut == 'protection':
                attributs[attribut] = randint(1, 10) / 1000
            else:
                attributs[attribut] = randint(1, 10)
            Things(
                name=choice(Things.NAMES),
                protection=attributs['protection'],
                attack=attributs['attack'],
                hp=attributs['hp']
            )
        Things.items.sort(key=lambda item: item.protection)


class Person:
    """class for fighters"""

    NAMES = [
        'Sento', 'Artas', 'Capell', 'Garrus', 'Alistair',
        'Leliana', 'Afro', 'Aya', 'Eiji', 'Tullius',
        'Jolee', 'Valens', 'Yuthura', 'Master Li', 'Canderous',
        'Katarina', 'Ashe', 'Andriel', 'Rikku', 'Darth Sion'
    ]

    fighters = []
    losers = []

    def __init__(self, name, hp, attack, protection):
        self.name = name
        self.HitPoints = hp
        self.attack_damage = attack
        self.finalProtection = protection
        self.items = []
        self.fighters.append(self)

    def setThings(self, things):
        self.items.append(things)
        self.characteristic_calculator()

    def receive_damage(self, damager):
        self.HitPoints -= (
            damager.attack_damage -
            round(damager.attack_damage * self.finalProtection, 2)
        )

    def characteristic_calculator(self):
        self.HitPoints = self.HitPoints + sum(item.hp for item in self.items)
        self.attack_damage = (
                self.attack_damage +
                sum(item.attack for item in self.items)
        )
        self.finalProtection = (
                self.finalProtection +
                sum(item.protection for item in self.items)
        )
        if self.finalProtection > 0.5:
            self.finalProtection = 0.5

    def fight(self, fighter_2):
        damage = round((
            fighter_2.attack_damage -
            (fighter_2.attack_damage * self.finalProtection)), 2
            )
        self.receive_damage(fighter_2)
        print(Fore.WHITE + f'{fighter_2.name} наносит удар по {self.name} '
              f'на {damage} урона')
        if self.HitPoints <= 0:
            print(Fore.RED + f'{self.name} убит!')
            Person.losers.append(
                Person.fighters.pop(Person.fighters.index(self))
            )

    @staticmethod
    def create_fighters():
        for _ in range(10):
            attributs = {
                'protection': randint(5, 15)/100,
                'attack': randint(6, 10),
                'hp': randint(100, 200)
            }
            fighter_class = choice(['Pal', 'War'])
            if fighter_class == 'Pal':
                Paladin(
                    name=Person.NAMES.pop(randrange(0, len(Person.NAMES))),
                    hp=attributs['hp'],
                    attack=attributs['attack'],
                    protection=attributs['protection']
                )
            else:
                Warior(
                    name=Person.NAMES.pop(randrange(0, len(Person.NAMES))),
                    hp=attributs['hp'],
                    attack=attributs['attack'],
                    protection=attributs['protection']
                )

    @staticmethod
    def to_arms():
        temp_fighter_list = Person.fighters.copy()
        while len(temp_fighter_list) > 0 and len(Things.items) > 0:
            fighter = choice(temp_fighter_list)
            item = choice(Things.items)
            fighter.setThings(item)
            Things.items_in_use.append(Things.items.pop(
                Things.items.index(item)
                ))
            if len(fighter.items) > 3:
                temp_fighter_list.remove(fighter)

    @staticmethod
    def battle():
        print(Fore.GREEN + 'Да начнется битва!!!')
        while len(Person.fighters) > 1:
            fighter = choice(Person.fighters)
            fighter_2 = choice(Person.fighters)
            if fighter_2 == fighter:
                fighter_2 = choice(Person.fighters)
            fighter.fight(fighter_2)
        print(
            Fore.GREEN +
            f'Битва окончена! Победитель - {Person.fighters[0].name}! '
            'Хвала чемпиону!'
        )

    @staticmethod
    def go_to_arena():
        Things.generate_items()
        Person.create_fighters()
        Person.to_arms()
        Person.battle()


class Paladin(Person):
    """Tank class"""

    def __init__(self, name, hp, attack, protection):
        super().__init__(name, hp, attack, protection)
        self.HitPoints = hp * 2
        self.finalProtection = protection * 2


class Warior(Person):
    """Damagedealer class"""

    def __init__(self, name, hp, attack, protection):
        super().__init__(name, hp, attack, protection)
        self.attack_damage = attack * 2


if __name__ == '__main__':
    Person.go_to_arena()
