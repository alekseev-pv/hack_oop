from game_classes import Thing, Warrior, Paladin, Arena, PersonsGenerator

if __name__ == "__main__":
    things = [
        Thing("Булава ярости", 0, -0.1, 40),
        Thing("Обычный меч", 0, 0, 15),
        Thing("Топор гнома", 0, 0, 20),
        Thing("Щит милосердия", 0, 0.05, 0),
        Thing("Стальная кираса", 20, 0.1, 0),
        Thing("Сапоги", 0, 0.05, 0),
        Thing("Кольцо здоровья", 20, 0, 0),
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

    hg = PersonsGenerator(names_person)
    persons = hg.get_persons(10)

    arena = Arena(persons, things)
    arena.equip_randomly()
    arena.fight()

    print()
