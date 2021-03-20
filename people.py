class Person:
    """Base class for a character"""
    def __init__(self, name, hp, base_attack, base_def):
        self.name = name
        self.health = hp
        self.base_attack = base_attack
        self.base_defence = base_def
        self.things = []

    def set_things(self, things):
        self.things = things
        self.add_params()

    def get_hit(self, attacker):
        attack_damage = attacker.get_base_attack()
        final_protec = self.get_base_defence() / 100
        attack_damage -= attack_damage * final_protec
        attack_damage = round(attack_damage, 2)
        if self.health > 50 > self.health - attack_damage:
            if self.things:
                item = self.things.pop(0)
                self.base_attack -= item.attack
                self.base_defence -= item.defence
                self.health -= item.health
        self.health = self.health - attack_damage if self.health - attack_damage > 0 else 0
        self.health = round(self.health, 2)
        print(f'{attacker} наносит удар по {self.name} на {attack_damage} урона')


    def get_base_attack(self):
        return self.base_attack

    def get_base_defence(self):
        return self.base_defence

    def get_health(self):
        return self.health

    def add_params(self):
        add_attack = sum(t.attack for t in self.things)
        add_defence = sum(t.defence for t in self.things)
        add_health = sum(t.health for t in self.things)
        self.base_attack = self.base_attack + add_attack if self.base_attack + add_attack <= 110 else 110
        self.base_defence = self.base_defence + add_defence if self.base_defence + add_defence <= 110 else 110
        self.health = self.health + add_health if self.health + add_health <= 110 else 110

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Paladin(Person):
    def __init__(self, name, hp, base_attack, base_def):
        super().__init__(name, hp * 2, base_attack, base_def * 2)


class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_def):
        super().__init__(name, hp, base_attack * 2, base_def)
