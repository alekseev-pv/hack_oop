from game_classes import (
    Thing,
    Warrior,
    Paladin,
    Arena,
    PersonsGenerator,
    Player,
    NameGenerator,
)

if __name__ == "__main__":
    # сортировка в арене
    things = [
        Thing("Булава ярости", 0, -0.1, 40),
        Thing("Обычный меч", 0, 0, 15),
        Thing("Топор гнома", 0, 0, 20),
        Thing("Щит милосердия", 0, 0.05, 0),
        Thing("Стальная кираса", 0.2, 0.1, 0),
        Thing("Сапоги", 0, 0.05, 0),
        Thing("Кольцо здоровья", 0.20, 0, 0),
        Thing("Кольцо защиты", 0, 0.1, 0),
        Thing("Кольцо бешенства", 0, -0.05, 15),
    ]

    names_person = [
        "Анлион",
        "Дайладор",
        "Бранэджил",
        "Демпдеин",
        "Гарелтис",
        "Макшусен",
        "Вильоса",
        "Киерира",
        "Келдерлин",
        "Джеингхэйл",
        "Маднаста",
        "Генелми",
        "Габседа",
        "Джастевард",
        "Магнагель",
        "Хейлакус",
        "Аверлихен",
        "Айсмор",
        "Каеронна",
        "Альпдетор",
        "Дамриган",
    ]

    nouns = [
        "Топор",
        "Дубина",
        "Меч",
        "Кираса",
        "Кольцо",
        "Щит",
        "Сапоги",
        "Кольчуга",
    ]
    subjects = [
        "Алчности",
        "Бестрашия",
        "Бешенства",
        "Трусости",
        "Всевластия",
        "Доброты",
        "Смелости",
        "Чести",
        "Духа",
        "Силы",
    ]

    names_thing_gen = NameGenerator(nouns, subjects)
    names_thing = names_thing_gen.get_names(20)

    persons_gen = PersonsGenerator(names_person)
    persons = persons_gen.get_persons(10)

    player = Player("Ivan")
    # персонажа можно создать через консоль
    # player.create_person()
    player_person = Warrior(
        name="+++KaPaTe/I+++", hit_points=100, protection=20, attack_damage=20
    )

    player.set_person(player_person)
    player.person.set_inventory([])
    player.take_thing(Thing("Обычный меч", 0, 0, 15))
    player.take_thing(Thing("Обычный меч", 0, 0, 15))
    player.take_thing(Thing("Кольцо бешенства", 0, -0.05, 15))
    player.take_thing(Thing("Сапоги", 0, 0.05, 0))

    arena = Arena(persons, things)
    arena.equip_randomly()
    arena.add_player(player)
    winner = arena.fight()

    print(f"ИИИИ победитель {winner}")
