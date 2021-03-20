from persons import Paladin, Warrior, Goblin, Elf
from arena import Arena
import re


class ArenaPlayerBot(Arena):
    CLASS_PERSONS = {'паладин': Paladin, 'воин': Warrior, 'гоблин': Goblin, 'эльф': Elf}

    def __init__(self, name_arena):
        super().__init__(name_arena)
        self.size_persons = None
        self.class_person = None
        self.names_persons = None

    def get_parameter_from_player(self):
        pattern = r', |,| '
        get_parametrs = input('Введите размер отряда, класс персонажей(Паладин, Воин, Гоблин, Эльф:\n'
                              'Пример: 3, паладин\n')
        self.size_persons, self.class_person = re.split(pattern, get_parametrs)
        while 1:
            if self.size_persons.isdigit():
                self.size_persons = int(self.size_persons)
                break
            self.size_persons = input('Вы ошиблись при вводе размера отряда.\nВведите размер отряда (число):\n')

        while 1:
            if self.class_person.lower() in self.CLASS_PERSONS:
                self.class_person = self.CLASS_PERSONS[self.class_person.lower()]
                break
            self.class_person = input('Вы ошиблись при вводе класса персонажа.\n'
                                      'Напишите класс персонажей(Паладин, Воин, Гоблин, Эльф\n')
        self.names_persons = re.split(pattern, input('Напишите имена игроков\n'))
        if len(self.names_persons) < self.size_persons:
            pass


if __name__ == '__main__':
    name_thing = {
        'голова': ('шляпа', 'шлем', 'косынка'),
        'тело': ('плащ', 'броня', 'роба', 'балахон'),
        'оружие': ('меч', 'булава', 'бластре', 'лук и стрелы', 'арбалет', 'нож',),
        'шит': ('круглы щит', 'малый щит', 'большой щит', 'кожанный щит',),
        'обувь': ('кеды', 'ботинки', 'сапоги',),
        'украшения': ('кольцо', 'амулет', 'браслет',),
    }
    name_bot = ('Sandra_bot', 'Graham_bot', 'Joann_bot', 'Phelps_bot', 'Charles_bot', 'Long_bot',
                'Joyce_bot', 'Johnson_bot', 'Jerry_bot', 'Yates_bot', 'Linda_bot', 'Morris_bot',
                'Patricia_bot', 'Matthews_bot', 'Katherine_bot', 'Walker_bot', 'Linda_bot',
                'Morales_bot', 'Jared_bot', 'Williams_bot',)
    flag = 1
    while flag:
        name_arena = input('Королевская битва начинается! Введите название арены:\n')
        arena = ArenaPlayerBot(name_arena)
        arena.get_parameter_from_player()
        arena.create_persons(arena.names_persons, count=arena.size_persons, get_person=arena.class_person)
        print(f'Создан Ваш отряд:\n{arena.get_persons()}')
        arena.create_persons(name_bot, count=arena.size_persons)
        print('Создан отряд противника')
        print('Идет раздача снаряжения')
        arena.creating_things(name_thing)
        arena.give_things_persons()
        print('')
        arena.battle()
        flag = input('Чтобы сыграть еще раз введите любой символ и нажмите Enter.\n'
                     'Для выхода прочто нажмите Enter')
