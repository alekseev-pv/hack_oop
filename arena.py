from things import Thing
from persons import Paladin, Warrior, Person
import random


class Arena:
    def __init__(self, name):
        self.name = name
        self._things = []
        self._persons = []

    def __str__(self):
        return self.name

    def get_things(self):
        return self._things

    def get_persons(self):
        return self._persons

    def creating_things(self, name_thing, start=10, end=15):
        for _ in range(random.randint(start, end)):
            type_thing = name_thing[random.choice(list(name_thing))]
            name = type_thing[random.randint(0, len(type_thing) - 1)]
            defense_percentage = random.uniform(0.01, 0.1)
            attack = random.random()
            life = random.random()
            self._things.append(Thing(name, defense_percentage, attack, life))
        self._things.sort(key=lambda x: x.defense)

    def create_persons(self, name_persons, count=10):
        class_persons = (Paladin, Warrior)
        for _ in range(count):
            name = random.choice(name_persons)
            while name in [person.name for person in self._persons]:
                name = random.choice(name_persons)
            hp = random.randint(50, 100)
            attack = random.randint(10, 30)
            defense_percentage = random.randint(10, 40)
            class_person = random.choice(class_persons)
            self._persons.append(class_person(name, hp, attack, defense_percentage))

    def give_things_persons(self):
        for person in self.get_persons():
            count_thing = random.randint(0, 4)
            things = random.sample(self.get_things(), k=count_thing)
            person.set_things(things)

    def get_one_person(self):
        return self.get_persons().pop(random.randint(0, len(self.get_persons())-1))

    def battle(self):
        while len(self.get_persons()) > 1:
            first_person = self.get_one_person()
            second_person = self.get_persons()[random.randint(0, len(self.get_persons())-1)]
            first_person.update_hp_after_attack(second_person)
            count_damage = second_person.attack_damage - second_person.attack_damage * first_person.final_protection
            print(f'{second_person} наносит удар по {first_person} на {count_damage: .2f} урона')
            if first_person.is_alive:
                self._persons.append(first_person)

        print(f'Battle win {self.get_persons()[0]}')


if __name__ == '__main__':
    name_thing = {
        'head': ('hat', 'helmet', 'cap'),
        'body': ('sweater', 'chain', 'robe', 'hoodie'),
        'arms': ('gloves',),
        'legs': ('pants',),
        'feet': ('sneakers', 'boots', 'ballroom slippers',),
        'jewelry': ('ring', 'amulet', 'chain',),
    }

    name_persons = ('Sandra', 'Graham', 'Joann', 'Phelps', 'Charles', 'Long',
                   'Joyce', 'Johnson', 'Jerry', 'Yates', 'Linda', 'Morris',
                   'Patricia',  'Matthews', 'Katherine', 'Walker', 'Linda',
                   'Morales', 'Jared', 'Williams',)

    arena = Arena('Колизей')
    arena.creating_things(name_thing)
    arena.create_persons(name_persons)
    arena.get_things()
    arena.battle()





