import random, time

import colorama
from colorama import Fore, Style

import constants
from classes import Thing, Warrior, Paladin


def get_fighters(number=10):
    """
    Выбираем кандидатов из списка участников
    """
    temporary_names = constants.NICKNAMES
    names = []
    fighters = []
    for index in range(number):
        name = random.choice(temporary_names)
        names.append(name)
        temporary_names.remove(names[index])
        fighter = random.choice(
            [Warrior(person_name=name),
            Paladin(person_name=name)]
        )
        fighters.append(fighter)
    return fighters

def generate_thing_parameters():
    """
    Генерируем случайный набор параметров для вещи
    """
    name = ( 
        random.choice(constants.FIRST_PARAMETR) + ' ' +
        random.choice(constants.SECOND_PARAMETR) + ' ' +
        random.choice(constants.THIRD_PARAMETR)
    )
    protection = round(random.randint(1, 10) / 100, 2)
    power = random.randint(1, 100)
    healpoints = random.randint(1, 100)
    thing = [name, protection, power, healpoints]
    return thing

def create_things(count=20):
    """
    Создаем определенной количество (count) вещей
    """
    things = []
    for i in range(count):
        name, protection, power, healpoints = generate_thing_parameters()
        thing = Thing(name, protection, power, healpoints)
        things.append(thing)
    things.sort(key=lambda person: person.protection)
    return things

def get_dressed(fighters, things):
    """
    Разбираем шмотки
    """
    print(Fore.YELLOW + '\nКрутим рулетку по выдаче вещей !!!\n' + Fore.GREEN)
    time.sleep(1)
    for thing in things:
        hero = random.choice(fighters)
        if len(hero.things) == 4:
            print(len(fighters))
            continue
        hero.things.append(thing)
        hero.set_things(thing)  
        print(f'{hero.person_name} получил {thing.name}')
        things.remove(thing)
    time.sleep(1)

def fight(defender, attacker):
    """
    Проведение боя до победы между двумя бойцами.
    Возврашаем [победитель, проигравший]
    """
    colorama.init()
    hit_number = 1
    while defender.is_alive() and attacker.is_alive():
        print(
            Fore.GREEN + f'\nРаунд {hit_number} между '
            f'Защитником {defender.person_name} и' 
            f'Нападающим {attacker.person_name}\n' + Fore.RED
        )
        defender.get_attacked(attacker)
        if not defender.is_alive():
            print(
                Fore.GREEN +
                f'\nПобедитель в этом бою Атакующий {attacker.person_name}' + 
                Style.RESET_ALL
            )
            print(Style.RESET_ALL)
            return {'winner': attacker, 'looser': defender}
        attacker.get_attacked(defender)
        if not attacker.is_alive():
            print(Fore.GREEN +
            f'\nПобедитель в этом бою Защитник {defender.person_name}' +
            Style.RESET_ALL
        )
            return {'winner': defender, 'looser': attacker}
        hit_number += 1
        time.sleep(1)

def battle():
    print(Fore.GREEN)
    fighters = get_fighters()
    get_dressed(fighters, create_things())
    print(Fore.YELLOW + '\nПоприветствуем наших бойцов!!!' + Fore.GREEN)
    for fighter in fighters:
        print(fighter)
    while len(fighters) > 1:
        print(Fore.YELLOW + '\nНовый бой начинается !!!!!!\n' + Fore.GREEN)
        time.sleep(2)
        defender, attacker = random.sample(fighters, 2)
        pair = fight(defender, attacker)
        print(
            Fore.RED +
            f"{pair['looser'].person_name} покидает Арену" +
            Fore.GREEN
        )
        fighters.remove(pair['looser'])
    print(
        Fore.YELLOW + '*'*20 +
        f'\nПоздравляем победителя в соревновании {fighters[0].person_name}\n' +
        '*'*20 + Style.RESET_ALL
    )


if __name__ == "__main__":
    battle()
    


