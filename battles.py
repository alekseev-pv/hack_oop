'''Бои.'''
import datetime as dt
import random

from persons import Paladin, Person, Warrior
from things import Thing

THINGS_NAMES = ('Топор',
                'Меч',
                'Фляга',
                'Кольцо',
                'Артефакт',
                'Плащ',
                'Лук',
                'Книга',
                'Нечто',
                )

NAMES = ('Колобок',
         'Максимка',
         'Лин',
         'Скотт',
         'Доктор',
         'Алиен',
         'Борец',
         'Скучный',
         'Дровосек',
         'Алёнка',
         'Бобёр',
         'Свой',
         'Дурень',)

PERSONS = (Paladin, Warrior)


class Battle:
    ''' Битва.'''
    def __init__(self,
                 max_time: int = 10):
        self.max_time = max_time
        self.things = []
        self.things.sort()
        self.players_on_arena = []

    def __str__(self):
        return '\t'.join([str(player) for player in self.players])

    def __generate_thing__(self):
        '''Создаем случайную вещь.'''
        return Thing(THINGS_NAMES[random.randrange(0, len(THINGS_NAMES))],
                     random.randint(0, 10),
                     random.randint(0, 10),
                     random.randint(0, 10))

    def fill_things(self, things_count: int = 40):
        '''Формируем набор вещей.'''
        self.things = [self.__generate_thing__()
                       for i in range(things_count)]

    def __generate_person__(self, name):
        '''Создаем случайного персонажа.'''
        number_of_lives = random.randint(1, 2)
        attack = random.randint(1, 2)
        defense_percentage = random.randint(1, 10)
        return PERSONS[random.randrange(0, len(PERSONS))](name,
                                                          number_of_lives,
                                                          attack,
                                                          defense_percentage)

    def fill_persons(self, players_count: int = 10):
        '''Набираем случайных игроков.'''
        def random_list(size):
            rand_list = [i for i in range(size)]
            while len(rand_list) > 0:
                yield rand_list.pop(random.randrange(0, len(rand_list)))

        max_players_count = len(NAMES)
        if players_count > max_players_count:
            print(f'У нас всего {max_players_count} бойцов')
        players_count = min(max_players_count, players_count)
        count = random_list(players_count)

        self.players = [self.__generate_person__(NAMES[next(count)])
                        for i in range(players_count)]

    def choose_things(self):
        '''Раздаёт игрокам вещи, если повезёт.'''
        for i in range(4):
            for player in self.players:
                if len(self.things) > 0:
                    lucky = random.randint(0, 1)
                    if lucky == 1:
                        player.add_thing(self.things.pop(0))

    def choose_players(self, count):
        '''Выводит игроков из строя на арену.'''
        for i in range(count):
            player = self.players.pop(random.randrange(0, len(self.players)))
            self.players_on_arena.append(player)

    def return_players(self):
        '''Возвращает живых игроков в строй.'''
        for player in self.players_on_arena:
            if player.number_of_lives > 0:
                self.players.append(player)
        self.players_on_arena = []

    def attack_damage(self, attacking: Person, defender: Person):
        '''Атака.'''
        attack_damage = (attacking.attack -
                         attacking.attack *
                         defender.defense_percentage / 100)
        attack_damage = int(round(attack_damage, 0))
        defender.number_of_lives -= attack_damage
        print(f'{attacking.name} наносит удар по {defender.name} '
              f'на {attack_damage} урона')

    def fight(self):
        '''Бой. Игроки бьются случайным образом.'''
        timer = (dt.datetime.now() +
                 dt.timedelta(seconds=self.max_time))
        attacking_num = random.randrange(0, len(self.players_on_arena))
        defender_num = (attacking_num + 1) % len(self.players_on_arena)

        while timer > dt.datetime.now():
            attacking_num = random.randrange(0, len(self.players_on_arena))
            defender_num = (attacking_num + 1) % len(self.players_on_arena)
            self.attack_damage(self.players_on_arena[attacking_num],
                               self.players_on_arena[defender_num])
            if self.players_on_arena[defender_num].number_of_lives <= 0:
                print(f'{self.players_on_arena[defender_num].name} погиб :(')
                self.players_on_arena.pop(defender_num)

            if len(self.players_on_arena) < 2:
                break
        else:
            print('Время вышло.')
