import random
import time
from typing import List, Any


class Thing():

    name: str
    defense: float
    attack: float
    life: float

    def __init__(self, name, defense, attack, life):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.life = life


class Person():

    name: str
    hp: float
    base_attack: float
    base_defense: float
    things: List[Thing] = []

    def __init__(self, name, hp, base_attack, base_defense):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_defense = base_defense

    def __str__(self) -> str:
        return self.name

    def set_things(self, things: List[Thing]) -> None:
        self.things = things
        self.hp += sum(x.life for x in things)

    def take_damage(self, damage):
        self.hp -= damage


class Paladin(Person):
    def __init__(self,
                 name: str,
                 hp: float,
                 base_attack: float,
                 base_defense: float):
        Person.__init__(self, name, hp * 2, base_attack, base_defense * 2)


class Warrior(Person):
    def __init__(self,
                 name: str,
                 hp: float,
                 base_attack: float,
                 base_defense: float):
        Person.__init__(self, name, hp, base_attack * 2, base_defense)


all_things: List[Thing] = [
    Thing(name='Shield', defense=0.1, attack=0.01, life=0.2),
    Thing(name='Lance', defense=0.05, attack=0.04, life=0.1),
    Thing(name='Dagger', defense=0.05, attack=0.03, life=0.2),
    Thing(name='Crossbow', defense=0.04, attack=0.02, life=0.2),
    Thing(name='Machete', defense=0.07, attack=0.05, life=0.3),
    Thing(name='Hammer', defense=0.02, attack=0.02, life=0.3),
    Thing(name='Sword', defense=0.05, attack=0.04, life=0.2),
    Thing(name='Helmet', defense=0.09, attack=0.01, life=0.1),
    Thing(name='Hauberk', defense=0.08, attack=0.02, life=0.1),
    Thing(name='MagicRing', defense=0.1, attack=0.1, life=0.4)]

all_things.sort(key=lambda x: x.defense)

names: List[str] = [
    'Bjorn', 'Agwid', 'Aswald', 'Bo', 'Vicar',
    'Gustav', 'Sigrid', 'Karl', 'Mody', 'Orm',
    'Ormar', 'Rerik', 'Swan', 'Snorr', 'Tir',
    'Aspen', 'Vidgis', 'Trjud', 'Dietmar', 'Frigg']


def create_fighters_by_names(names: List[str]) -> List[Person]:
    persons: List[Person] = []
    for name in names:
        data: dict = {'name': name}
        data['hp'] = random.triangular(0.01, 0.25)
        data['base_attack'] = random.triangular(0.01, 0.25)
        data['base_defense'] = random.triangular(0.01, 0.25)

        if random.randint(0, 1):
            persons.append(Paladin(**data))
        else:
            persons.append(Warrior(**data))
    return persons


def to_equip(persons: List[Person]) -> None:

    things: List[Thing]

    for person in persons:
        things = random.sample(all_things, k=random.randrange(1, 5))
        person.set_things(things)


def fighting(fighters: List[Person]) -> None:

    attacker: Person
    defender: Person
    final_protection: float
    attack_damage: float
    damage: float

    while len(fighters) > 1:
        attacker, defender = random.sample(fighters, k=2)
        final_protection = (defender.base_defense +
                            sum(x.defense for x in defender.things))
        attack_damage = (attacker.base_attack +
                         sum(x.attack for x in attacker.things))
        damage = attack_damage * (1 - final_protection)
        defender.take_damage(damage)
        print(f'{attacker} наносит удар по {defender} на {damage:.2f} урона')
        if defender.hp <= 0:
            print(f'{defender} погиб!')
            fighters.remove(defender)
            print(f'И их осталось {len(fighters)}')
        time.sleep(1)
    print(f'Победитель {fighters[0]}!!!')


if __name__ == '__main__':

    user_name: str = input('Введите своё имя [random]: ')
    count_of_fighters: int = 9
    in_data: Any = None
    valid_count: bool = False
# username
    if user_name == '':
        user_name = random.choice(names)
    print(f'Вашего героя зовут {user_name}')
# count of fighters
    while valid_count is False:
        in_data = input('Введите число Ваших соперников от 1 до 19 [9]:')
        if in_data != '':
            try:
                in_data = int(in_data)
                if 0 < in_data < 20:
                    count_of_fighters = in_data
                    break
            except ValueError:
                continue
        valid_count = True

    time.sleep(1)
    chosen_names = random.sample(names, k=count_of_fighters)
    chosen_names.append(user_name)
    fighters = create_fighters_by_names(chosen_names)
    to_equip(fighters)
    fighting(fighters)
