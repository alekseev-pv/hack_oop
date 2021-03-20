import random
from main import *


helmet = Thing('helmet', 0.05, 0, 10)
armor = Thing('armor', 0.1, 0, 15)
pants = Thing('pants', 0.08, 0, 7)
gloves = Thing('gloves', 0.03, 0, 5)
boots = Thing('boots', 0.05, 0, 4)
sword = Thing('sword', 0, 12, 0)
bow = Thing('bow', 0, 15, 0)
shield = Thing('shield', 0.1, 0, 0)

things = [helmet, armor, pants, gloves, boots, sword, bow, shield]
things.sort(key=lambda thing: thing.thing_protection)

names = ['Дональд Серроне', 'Конор Макгрегор', 'Тони Фергюсон', 'Хорхе Масвидаль',
         'Хабиб Нурмагомедов', 'Джон Джонс', 'Аманда Нунес', 'Валентина Шевченко',
         'Вэйли Жанг', 'Стипе Миочич', 'Алекс Перез', 'Александр Пантожа', 'Аскар Аскаров',
         'Дэн Хукер', 'Пол Фелдер', 'Исраэль Адесанья', 'Камару Усман', 'Генри Сехудо',
         'Александр Волкановски', 'Алистар Оверим']

person_1 = Paladin(random.choice(names), 0.05, 10, 100)
person_2 = Paladin(random.choice(names), 0.06, 11, 100)
person_3 = Paladin(random.choice(names), 0.07, 12, 100)
person_4 = Paladin(random.choice(names), 0.08, 13, 100)
person_5 = Paladin(random.choice(names), 0.09, 14, 100)
person_6 = Warrior(random.choice(names), 0.05, 10, 100)
person_7 = Warrior(random.choice(names), 0.06, 11, 100)
person_8 = Warrior(random.choice(names), 0.07, 12, 100)
person_9 = Warrior(random.choice(names), 0.08, 13, 100)
person_10 = Warrior(random.choice(names), 0.09, 14, 100)

persons = [person_1, person_2, person_3, person_4, person_5,
           person_6, person_7, person_8, person_9, person_10]

number_of_things = random.randint(1, 4)

for person in persons:
    person.set_things(random.sample(things, number_of_things))

for person in persons:
    print(person.person_name, person.person_protection, person.person_attack, person.person_health)
