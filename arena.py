from things import Thing
from persons import Paladin, Warrior, Goblin, Elf
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
            defense = random.uniform(0.01, 0.1)
            attack = random.randint(-10, 10)
            hit_poins = random.randint(-10, 10)
            for_name = {defense: 'улучшеная защита', attack: 'улучшеная атака', hit_poins: 'больше здоровья'}
            best_property = max(defense, attack, hit_poins)
            name = f'{name} {for_name[best_property]}'
            self._things.append(Thing(name, defense, attack, hit_poins))
        self._things.sort(key=lambda x: x.defense)

    def create_persons(self, name_persons, count=10):
        class_persons = (Paladin, Warrior, Goblin, Elf)
        names = random.sample(name_persons, k=count)
        for i in range(count):
            name = names[i]
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
            else:
                how = random.choice(['достойно', 'отважно', 'безрассудно', 'смело'])
                print(f'{first_person} - пал. Он сражался {how}!')
        winner = self.get_persons()[0]

        things = ', '.join(map(str, winner.things)) if winner.things else 'не брал'
        print(f'Битву выиграл {winner}.\nОставшееся здоровье - {winner.hit_points: .1f}, '
              f'урон - {winner.attack_damage: .1f}, '
              f'защита - {winner.defense: .1f}, '
              f'вещи - {things}.'
              )


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
    arena.give_things_persons()
    arena.battle()





