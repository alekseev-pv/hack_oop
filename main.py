from game_classes import Thing, Warrior, Person, Paladin, Arena

if __name__ == "__main__":
    things = [
        Thing("Булава ярости", 0, -0.1, 20),
        Thing("Щит милосердия", 0, 0.1, 0),
    ]

    persons = [
        Warrior("Ульфрик", 100, 0.1, 15),
        Paladin("Тейтидан", 100, 0.1, 15),
    ]

    arena = Arena(persons, things)
    arena.equip_randomly()

    print()
