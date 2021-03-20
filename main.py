from game_classes import (Arena, NameGenerator, Paladin, PersonsGenerator,
                          Player, Thing, ThingsGenerator, Warrior)

if __name__ == "__main__":

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
    things_gen = ThingsGenerator(names_thing)
    things = things_gen.get_things()

    persons_gen = PersonsGenerator(names_person)
    persons = persons_gen.get_persons(10)

    player = Player("Ivan")
    # персонажа можно создать через консоль
    # player.create_person()
    player_person = Warrior(
        name="+++KaPaTe/l+++", hit_points=100, protection=0, attack_damage=20
    )

    player.set_person(player_person)
    player.take_thing(Thing("Обычный меч", 0, 0, 15))
    player.take_thing(Thing("Обычный меч", 0, 0, 15))
    player.take_thing(Thing("Кольцо бешенства", 0, -0.05, 15))
    player.take_thing(Thing("Сапоги", 0, 0.05, 0))

    arena = Arena(persons, things)
    arena.equip_randomly()
    arena.add_player(player)
    winner = arena.fight()

    print(f"ИИИИ победитель {winner}")
