class Things:
    """
    Класс содержит в себе следующие параметры
     - название, процент защиты, атаку и жизнь;
     Это могут быть предметы одежды, магические кольца, всё что угодно)
    """

    name: str
    per_protection: float
    attack: float
    life_points: float

    def __init__(self, name, per_protection, attack, life):
        self.name = name
        self.per_protection = per_protection
        self.attack = attack
        self.life_points = life

    def __repr__(self):
        return self.name
