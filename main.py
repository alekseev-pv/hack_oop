import Classes
from random import choice, randint, sample

a = Classes.Arena()
b = a.create_bots_with_things(10, 10)
for obj in b:
    print(f'{obj.name}, {obj.full_hp}, {obj.hp}, {obj.attack}, {obj.defense}')
a.bots_battle(b)

