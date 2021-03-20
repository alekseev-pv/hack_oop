import random

from main import Paladin, Thing, Warrior

# Вещи для бойцов
THINGS_FOR_FIGHTERS = {
    'шлем': Thing('шлем', 0.05, 0, 10),
    'доспехи': Thing('доспехи', 0.1, 0, 15),
    'штаны': Thing('штаны', 0.08, 0, 7),
    'перчатки': Thing('перчатки', 0.03, 0, 5),
    'ботинки': Thing('ботинки', 0.05, 0, 4),
    'меч': Thing('меч', 0, 12, 0),
    'лук': Thing('лук', 0, 15, 0),
    'щит': Thing('щит', 0.1, 0, 0)
}

# Бойцы UFC
names_of_fighters = ['Дональд Серроне', 'Конор Макгрегор', 'Тони Фергюсон',
                     'Хорхе Масвидаль', 'Хабиб Нурмагомедов', 'Джон Джонс',
                     'Брэндон Морено', 'Макс Холлоуэй', 'Ислам Махачев',
                     'Стипе Миочич', 'Алекс Перез', 'Александр Пантожа',
                     'Аскар Аскаров', 'Дэн Хукер', 'Пол Фелдер',
                     'Исраэль Адесанья', 'Камару Усман', 'Генри Сехудо',
                     'Александр Волкановски', 'Алистар Оверим']

things = []
fighters = []


def create_things() -> list:
    """Create a sorted list of items for the fighters."""
    for thing in THINGS_FOR_FIGHTERS.values():
        things.append(thing)
    things.sort(key=lambda article: article.thing_protection)
    return things


def create_fighters() -> list:
    """Creates a list of fighters."""
    for _ in range(5):
        fighter = Paladin(random.choice(names_of_fighters),
                          random.uniform(0.05, 0.1),
                          random.randint(70, 80), 100)
        names_of_fighters.remove(fighter.person_name)
        fighters.append(fighter)

    for _ in range(5):
        fighter = Warrior(random.choice(names_of_fighters),
                          random.uniform(0.05, 0.1),
                          random.randint(70, 80), 100)
        names_of_fighters.remove(fighter.person_name)
        fighters.append(fighter)
    return fighters


def dress_fighters() -> None:
    """Dress up the fighters."""
    for fighter in fighters:
        number_of_things = random.randint(1, 4)
        fighters_things = random.sample(things, number_of_things)
        fighter.set_things(fighters_things)


def game() -> None:
    """Start the game."""
    duel = 0
    print('Приветсвуем всех участников игры "Арена"!')
    print()
    print('Представляем вам бойцов:')

    for fighter in fighters:
        print(f'Имя бойца: {fighter.person_name}, '
              f'Защита бойца: {fighter.person_protection}, '
              f'Атака бойца: {fighter.person_attack}, '
              f'Здоровье бойца: {fighter.person_health}',
              'Вещи бойца: ', end='')
        for thing in fighter.person_things:
            print(f'{thing}', end=' ')
        print()
    print()
    print('Бои начинаются!')

    while len(fighters) > 1:
        print()
        duel += 1
        fight = random.sample(fighters, 2)
        print(f'В поединке №{duel} {fight[0]} наносит удар по {fight[1]} '
              f'на {fight[0].person_attack} урона')
        fight[1].damage_to_health(fight[0].person_attack)
        print(f'У {fight[1]} осталось {fight[1].person_health} здоровья')
        if fight[1].person_health <= 0:
            fighters.remove(fight[1])
            print(f'{fight[1]} выбывает из игры')
        if len(fighters) == 1:
            print()
            print(f'Победитель: {fighters[0]} '
                  f'с остатком здоровья {fighters[0].person_health}')


if __name__ == '__main__':
    things = create_things()
    fighters = create_fighters()
    dress_fighters()
    game()
