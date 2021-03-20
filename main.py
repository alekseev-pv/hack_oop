import random

from settings import BASE_SET, KINDS


class Thing():
    def __init__(self, name, protection, damage, life):
        self.name = name
        self.protection = protection
        self.damage = damage
        self.life = life

    def __str__(self):
        return (
            'Предмет: Название - {}, Защита - {}, Урон - {}, Жизнь - {}'.
            format(self.name, self.protection, self.damage, self.life)
        )


class Person():
    def __init__(self, name, protection, damage, life):
        self.name = name
        self.protection = protection
        self.damage = damage
        self.life = life
        self.current_life = life
        self.current_damage = damage
        self.finalProtection = protection
        # todo Присваивать названия классов в соответствии с полом персонажа
        self.type = 'Безклассовый'

    def stats_calc(self):
        self.current_life = self.life
        self.current_damage = self.damage
        self.finalProtection = self.protection
        for item in self.things:
            self.current_life += item.life
            self.finalProtection += item.protection
            self.current_damage += item.damage
        self.finalProtection = round(self.finalProtection, 2)
        return self

    def set_things(self, things):
        # todo Сделать алгоритм не допускающий, чтобы перс получал два шлема
        self.things = []
        if len(things) == 0:
            return self
        count = random.randint(1, 4)
        if count > len(things):
            count = len(things)
        for i in range(count):
            thing = random.choice(things)
            self.things.append(thing)
            things.remove(thing)
        self.stats_calc()
        return self

    def hp_decrease(self, attack_damage):
        self.current_life -= attack_damage * (1 - self.finalProtection)

    MSG = 'Персонаж: Имя - {}, Класс - {}, Защита - {}, Урон - {}, Жизнь - {}'

    def __str__(self):
        return (
            self.MSG.format(
                self.name, self.type, self.finalProtection,
                self.current_damage, self.current_life
            )
        )


class Paladin(Person):
    def __init__(self, name, protection, damage, life):
        Person.__init__(self, name, protection, damage, life)
        self.life *= 2
        self.protection *= 2
        self.type = 'Паладин'


class Warrior(Person):
    def __init__(self, name, protection, damage, life):
        Person.__init__(self, name, protection, damage, life)
        self.damage *= 2
        self.type = 'Воин'


CLASSES = [Person, Paladin, Warrior]


class BattlePrepare():
    def creation(self, kind, max_count):
        items = []
        if kind != 'thing' and kind != 'pers':
            raise TypeError('Не верный тип. Должен быть pers или thing')
        names = list(KINDS[kind].keys())
        count = 0
        if kind == 'pers':
            count = max_count
        else:
            count = random.randint(1, max_count)
        classname = None
        if kind == 'thing':
            classname = Thing
        for i in range(count):
            if kind == 'pers':
                classname = random.choice(CLASSES)
            items.append(
                classname(
                    random.choice(names),
                    round(
                        random.uniform(
                            BASE_SET[kind]['protection']['min'],
                            BASE_SET[kind]['protection']['max']
                        ), 2
                    ),
                    random.randint(
                        BASE_SET[kind]['dmg']['min'],
                        BASE_SET[kind]['dmg']['max']
                    ),
                    random.randint(
                        BASE_SET[kind]['life']['min'],
                        BASE_SET[kind]['life']['max']
                    ),
                )
            )
        return items


class TournamentGrid():
    def form(self, persons):
        self.pers = persons.copy()
        self.grid = []
        while len(self.pers) > 1:
            pers1 = random.choice(self.pers)
            self.pers.remove(pers1)
            pers2 = random.choice(self.pers)
            self.pers.remove(pers2)
            self.grid.append([pers1, pers2])
        return self

    def __str__(self):
        msg = '\r\nТурнирная сетка\r\n'
        i = 1
        for item in self.grid:
            if item[1] is not None:
                msg += '{}-й бой: {} {} против {} {}\r\n'.format(
                    i, item[0].type, item[0].name, item[1].type, item[1].name
                )
                i += 1
        return (msg)


class Arena():
    def one_round(self, persons, grid):
        first_strike = random.randint(0, 1)
        second_strike = 0
        for i in range(len(grid)):
            if i != first_strike:
                second_strike = i

        pers1 = grid[first_strike]
        pers2 = grid[second_strike]
        i = 0
        pers_loser = pers2
        pers_winner = pers1
        while pers1.current_life > 0 and pers2.current_life > 0:
            if i % 2 == 0:
                pers2.hp_decrease(pers1.current_damage)
                pers_loser = pers2
                pers_winner = pers1
            else:
                pers1.hp_decrease(pers2.current_damage)
                pers_loser = pers1
                pers_winner = pers2
            i += 1

        pers_winner.stats_calc()
        pers_loser.stats_calc()
        persons.remove(pers_loser)
        return 'побеждает {} {}'.format(pers_winner.type, pers_winner.name)

    def battle(self, max_persons, max_items):
        print('Это Арена, а не игра!')
        things = BattlePrepare().creation('thing', max_items)
        print('Created {} items'.format(len(things)))
        for item in things:
            print(item)
        persons = BattlePrepare().creation('pers', 10)
        print('Created {} persons'.format(len(persons)))
        for item in persons:
            item.set_things(things)
            print(item)
        print('\r\nДа начнется битва!')
        ind_r = 1  # Индекс раунда
        while len(persons) > 1:
            grid = TournamentGrid().form(persons)
            print(grid)
            ind_f = 1  # Индекс боя
            for fight in grid.grid:
                print(
                    'В {}-м бою {}-го раунда {}'.format(
                        ind_f, ind_r, self.one_round(persons, fight)
                    )
                )
                ind_f += 1
            ind_r += 1
        print(
            '\r\nПоздравляем победителя, {} {} !!!'.format(
                persons[0].type, persons[0].name
            )
        )


Arena().battle(10, 100)
