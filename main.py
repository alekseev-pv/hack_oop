import colorama
import random
import time
from typing import Optional

colorama.init()

class Thing:

    name_list = ['Кольцо безумия', 'Пояс неверности', 'Ксива', 'Фуражка',
                 'Полномочие', 'Неприкосновенность', 'Чистые носки',
                 'Грязные носки', 'Каска', 'Погоны', 'Мозг', 'Дубинка',
                 'Улики', 'Жетон', 'Форма', 'Травмат', 'Пистолет', 'Бабки',
                 'Ордер на безграничное насилие', 'Уголовный кодекс']

    def __init__(self):
        self.thing_name = random.choice(self.name_list)
        self.protection_bonus = round(random.uniform(0.01, 0.1), 3)
        self.atack_bonus = random.randrange(5, 20, 1)
        self.HP_bonus = random.randrange(10, 40, 3)

characters_name_list = ['Рядовой', 'Ефрейтор', 'Сержант', 'Старшина',
                            'Прапорщик', 'Лейтенант', 'Капитан', 'Майор',
                            'Подполковник', 'Полковник', 'Генерал-майор',
                            'Генерал-лейтенант', 'Генерал-полковник',
                            'Генерал армии', 'Маршал', 'Президент', 'Судья']

def generate_name(name_in_list):
    return f'{random.choice(name_in_list)}'


class Person:


    def __init__(self):
        self.person_name = generate_name(characters_name_list)
        self.hit_points = hit_points
        self.attack_damage = random.randrange(5, 15)
        self.base_def = random.uniform(0.1, 0.2)
        self.thing_list = []
        self.finalProtection = 0


class Paladin(Person):

    def __init__(self):
        self.person_name = generate_name(characters_name_list)
        self.hit_points = 2*random.randrange(100, 200)
        self.attack_damage = random.randrange(5, 15)
        self.base_def = random.uniform(0.1, 0.2)
        self.thing_list = []
        self.finalProtection = 0


class Warrior(Person):
    
    def __init__(self):
        self.person_name = generate_name(characters_name_list)
        self.hit_points = random.randrange(100, 200)
        self.attack_damage = 2*random.randrange(5, 15)
        self.base_def = random.uniform(0.1, 0.2)
        self.thing_list = []
        self.finalProtection = 0


class BattleArena:

    def __init__(self):
        self.thing_list_all = []
        self.list_characters = []
        self.battle_characters = []    

    def create_things(self):
        list_range = random.randrange(10, 20)
        while len(self.thing_list_all) != list_range:
            self.thing_list_all.append(Thing())
        print(self.thing_list_all)

    def create_user_pers(self, user_name, user_hp, p):
        self.p = p
        if self.p == 1:
            self.battle_characters.append(Paladin(user_name, user_hp))
        else:
            self.battle_characters.append(Warrior(user_name, user_hp))

    def create_characters(self):
        generated_list = []
        while len(generated_list) != 12:
            generated_list.append(Paladin())
            generated_list.append(Warrior())
        while len(self.battle_characters) != 10:
            rnd_char = random.choice(generated_list)
            self.battle_characters.append(rnd_char)

    def set_dress(self):
        for character in self.battle_characters:
            print(character)
            rndm_quintity = random.randrange(1, 4)
            rnd_things = random.sample(self.thing_list_all, rndm_quintity)
            character.thing_list = rnd_things
            for bonus in rnd_things:
                character.finalProtection = (character.base_def
                                             + bonus.protection_bonus)
                character.attack_damage = (character.attack_damage 
                                          + bonus.atack_bonus)
                character.hit_points = int(character.hit_points) + bonus.HP_bonus

    def start_battle(self):
        battle_ground = self.battle_characters
        while len(battle_ground) != 1:
            duel = random.sample(battle_ground, 2)
            atkr = duel[0]
            dfndr = duel[1]
            attacker = atkr.person_name
            defender = dfndr.person_name
            print("\033[31m\033[44m{}".format(
                  f"Драка: Атакует {attacker} - Защищается {defender}"))
            time.sleep(0.25)
            hit = int(atkr.attack_damage -
                      atkr.attack_damage*dfndr.finalProtection)
            print(f'{attacker} наносит удар в размере: {hit} по {defender}'+'у')
            dfndr.hit_points = dfndr.hit_points - hit
            if dfndr.hit_points >= 0:
                continue
            else:
                print("\033[37m\033[44m{}".format(f'{defender} помер от полученного урона от {attacker}'
                      +'a'))
                battle_ground.remove(dfndr)
        print("\033[31m\033[43m{}".format(f"Победитель {battle_ground[0].person_name}"))







# print('Добро пожаловать в МВД Арену')
# # time.sleep(2)
# input('Жми Enter, чтобы не сесть!')
# print('Молодец хорошо подчиняешься, так держать!')

# # time.sleep(1)
# print('Будешь драться(1) или смотреть(0)? (Введи цифру нажми Enter)')
# a = int(input())
# if a == 1:
#     print('Отлично')
#     print('Как тебя зовут?:')
#     user_name = input()
#     print('Сколько у тебя ХП?(только цифры, не ломай программу):')
#     user_hp = input()
#     print('Есть ли броня, поможет узнать пару ударов :)')
#     print('Ты паладин(1) или воин(0)? (Введи цифру нажми Enter):')
#     p = int(input())
#     if p == 1:
#         print('Палладин, ахахахахахахаха')
#         # time.sleep(1)
#         print('ах-аха-ха-хах-ахаха')
#         # time.sleep(1)
#         print('Ладно погнали!')
new_battle = BattleArena()
print('Создаю вещи')
new_battle.create_things()
# print('Добавляю твоего перса')
# new_battle.create_user_pers(user_name, user_hp, p)
print('Создаю противников!')
new_battle.create_characters()
print('Одеваю противников!')
new_battle.set_dress()
print('Нажми Enter чтобы увидеть сражение')
new_battle.start_battle()
#     elif p == 0:
#         print('Запомни, войн НЕ 0!')
#         # time.sleep(1)
#         print('Ладно погнали!')
#         new_battle = UserGame(user_name, user_hp, p)
#         new_battle.create_user_pers()
#     else:
#         print('Эльфы дальше по корридору!')
#         exit()
# else:
#     pass
