from things import Thing


class Person:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hit_points = hp
        self.attack_damage = attack
        self.defense = defense
        self.things = []

    @property
    def is_alive(self):
        if self.hit_points > 0:
            return True
        return False

    @property
    def final_protection(self):
        return round(self.defense / 100, 2)

    def set_things(self, things):
        for thing in things[:4]:
            self.things.append(thing)
            self.hit_points += thing.hit_poins
            self.attack_damage += thing.attack_damage
            self.defense += thing.defense_percentage * self.defense

    def update_hp_after_attack(self, other):
        if self.is_alive:
            self.hit_points -= (other.attack_damage - other.attack_damage * self.final_protection)

    def __str__(self):
        return f'{self.name}({self.__class__.__name__})'

    def __repr__(self):
        return f'{self.name}({self.__class__.__name__})'


class Warrior(Person):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.attack_damage *= 2


class Paladin(Person):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.hit_points *= 2
        self.defense *= 2


class Elf(Person):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.hit_points *= 1.1
        self.defense *= 1.2
        self.attack_damage += 15


class Goblin(Person):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.hit_points *= 3
        self.defense *= 2
        self.attack_damage *= 0.9


if __name__ == '__main__':
    paladin = Paladin('paladin', 10, 10, 10)
    warrior = Warrior('warrior', 10, 10, 10)
    person = Person('person', 10, 10, 10)
    print(paladin)
    print(warrior)
    print(person)


