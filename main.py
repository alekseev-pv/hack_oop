from random import choice, randint


class Thing:
    def __init__(self, name, bonus_defense, bonus_attack, bonus_hp):
        self.name = name
        self.bonus_defense = bonus_defense
        self.bonus_attack = bonus_attack
        self.bonus_hp = bonus_hp


class Person:
    def __init__(self, name, base_defense, base_attack, base_hp):
        self.name = name
        self.base_hp = base_hp
        self.base_defense = base_defense
        self.base_attack = base_attack
        self.result_defense = self.base_defense
        self.result_attack = self.base_attack
        self.result_hp = self.base_hp
        self.bonus_attack = 0
        self.bonus_defense = 0.0
        self.bonus_hp = 0
        self.wear_things = ''

    def set_things(self, things):
        self.wear_things = things
        for i in range(len(things)):
            self.bonus_defense += things[i].bonus_defense
            self.bonus_attack += things[i].bonus_attack
            self.bonus_hp += things[i].bonus_hp
        self.result_defense = (self.base_defense + self.bonus_defense) / 100
        self.result_attack = self.base_attack + self.bonus_attack
        self.result_hp = self.base_hp + self.bonus_hp

    def get_damage_from(self, enemy):
        received_damage = round(
            enemy.result_attack * (1 - self.result_defense)
            )
        self.result_hp -= received_damage
        print(f'{enemy.name} наносит удар по {self.name} на '
              f'{received_damage} урона')
        if self.result_hp <= 0:
            print(f'И {self.name} погибает')
            print()

    def turn(self):
        pass


class Paladin(Person):
    def __init__(self, name, base_defense, base_attack, base_hp):
        super().__init__(name, base_defense, base_attack, base_hp)
        self.base_hp = base_hp * 2
        self.base_defense = base_defense * 2


class Warrior(Person):
    def __init__(self, name, base_defense, base_attack, base_hp):
        super().__init__(name, base_defense, base_attack, base_hp)
        self.base_attack = base_attack * 2


def create_heroes(amount_h, amount_p):
    names1 = [
        'сомневающийся', 'хохочущий', 'потерявший страх', 'лукавый'
        ]
    names2 = [
        'Алеша', 'Чебурашка', 'Маг отшельник', 'Интроверт', 'Саня Пушкин',
        'Человек-видимка', 'Скрипач', 'Прохожий'
        ]
    hero = []
    for i in range(amount_h):
        base_hp = randint(100, 120)
        base_defense = randint(0, 20)
        base_attack = randint(10, 20)
        name_hero = choice(names1) + ' ' + choice(names2)
        if i <= amount_p - 1:
            class_person = Paladin
        else:
            class_person = Warrior
        hero.append(class_person(name_hero, base_defense,
                                 base_attack, base_hp))
    return hero


def create_list_all_things(amount):
    thing_name_half1 = [
        'халат', 'парик', 'шлепанцы', 'телогрейка',
        'масло для тела', 'блуза', 'носочки', 'чулки'
    ]
    thing_name_half2 = [
        'Синдром Котара', 'Прозопагнозия', 'Синестезия', 'Афантазия',
        'Одностороннее пространственное игнорирование', 'Синдром чужой руки'
    ]
    all_things = []
    for i in range(amount):
        composite_name = (choice(thing_name_half1) + ' ' +
                          choice(thing_name_half2))
        bonus_defense = randint(0, 10)
        bonus_attack = randint(0, 5)
        bonus_hp = randint(0, 20)
        all_things.append(Thing(composite_name, bonus_defense,
                                bonus_attack, bonus_hp))
        all_things = sorted(all_things,
                            key=lambda x: x.bonus_defense)
    return all_things


def dress_heroes(hero_list):
    def choose_things_for(hero_one):
        hero_list_things = []
        for i in range(randint(1, 4)):
            one_thing = list_all_things.pop(
                randint(0, len(list_all_things) - 1)
                )
            hero_list_things.append(one_thing)
        hero_one.set_things(hero_list_things)

    for i in range(len(hero_list)):
        choose_things_for(hero_list[i])


def battle(hero_list):
    while len(hero_list) > 1:
        defender = hero_list.pop(randint(0, len(hero_list) - 1))
        attacker = hero_list.pop(randint(0, len(hero_list) - 1))
        defender.get_damage_from(attacker)
        hero_list.append(attacker)
        if defender.result_hp > 0:
            hero_list.append(defender)

    print(f'Победил {hero_list[0].name} с {hero_list[0].result_hp} hp')


# Задать основные переменные
amount_heroes = 10
amount_paladins = randint(0, amount_heroes)
amount_warriors = amount_heroes - amount_paladins
max_things_for_one = 4
amount_things = amount_heroes * max_things_for_one

# Создать героев списком
heroes = create_heroes(amount_heroes, amount_paladins)

# Создать вещи списком
list_all_things = create_list_all_things(amount_things)

# Распределить вещи и одеть всех героев
dress_heroes(heroes)

# Битва до последнего выжившего хи-хи
battle(heroes)
