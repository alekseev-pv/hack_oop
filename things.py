class Thing:
    def __init__(self, name, defense, attack, hit_poins):
        self.name = name
        self.attack_damage = attack
        self.hit_poins = hit_poins
        self.defense = defense

    @property
    def defense_percentage(self):
        if self.defense > 0.1:
            return 0.1
        return self.defense

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'
