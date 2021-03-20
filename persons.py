from typing import List

from things import Things


class Person:
    name: str
    life_counter: float
    base_attack: float
    base_protection: float
    things: List[Things]

    all_life: float
    attack_damage: float
    final_protection: float

    def __init__(self, name, life_counter, base_attack, base_protection):
        """
        Принимает Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты.
        """
        self.name = name
        self.life_counter = life_counter
        self.base_attack = base_attack
        self.base_protection = base_protection

        self.all_life = 0
        self.attack_damage = 0
        self.final_protection = 0
        self.things = []

    def set_things(self, things: List[Things]):
        """
        Надеть на персонажа вещи из списка
        """
        self.things.extend(things)

    def get_stats_with_things_effect(self):
        """
        Применяем эффекты вещей к статам персонажа
        """

        self.all_life = (self.life_counter
                         + sum(thing.life_points for thing in self.things))

        self.final_protection = round(
            self.base_protection
            + (sum(thing.per_protection for thing in self.things)), 2)

    def get_attack_damage(self):
        return self.base_attack + sum(thing.attack for thing in self.things)

    def decrease_life(self, attacking) -> float:
        """
         У Защищающегося вызывается метод вычитания жизни на основе атаки
        (attack_damage) Нападающего.

        Количество получаемого урона рассчитывается по формуле:
        (attack_damage - attack_damage*finalProtection)

        Жизнь вычитается по формуле
         (HitPoints - (attack_damage - attack_damage*finalProtection)),
          где finalProtection - коэффициент защиты в десятичном виде;

        :param attack_damage: атака нападающего
        """
        attack_damage = attacking.get_attack_damage()
        self.get_stats_with_things_effect()
        damage = (attack_damage - attack_damage * self.final_protection)
        self.all_life = round(self.all_life - damage, 2)
        self.life_counter = round(self.life_counter - damage, 2)
        return damage


class Paladin(Person):
    """
    Паладин
    Стандартные жизнь и процент защиты умножаются на 2.
    """

    def __init__(self, name=None, life_counter=None,
                 base_attack=None, base_protection=None):
        super().__init__(name, life_counter, base_attack, base_protection)
        self.life_counter *= 2
        self.base_protection *= 2


class Warrior(Person):
    """
    Воин
    Стандартная атака умножается на 2.
    """

    def __init__(self, name=None, life_counter=None,
                 base_attack=None, base_protection=None):
        super().__init__(name, life_counter, base_attack, base_protection)
        self.base_attack *= 2


class CatDog(Person):
    """
    Котопёс
    Все показатели увеличены на 50%. Добавили в имя эту суперспособность
    """

    def __init__(self, name=None, life_counter=None,
                 base_attack=None, base_protection=None):
        super().__init__(name, life_counter, base_attack, base_protection)
        self.name += ' - Котопёс'
        self.life_counter *= 1.5
        self.base_protection *= 1.5
        self.base_attack *= 1.5
