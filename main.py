import random

names = ["Тор", "Конан", "Фесс", "Гром", "Зевс", 
        "Марс", "Один", "Геракл", "Зэна", "Диана", 
        "Афина", "Титан", "Спартак", "Гаргона", "Арагорн", 
        "Боромир", "Леонид", "Гор", "Онурис", "Нейт"]

# Выбор случайного имени из списка имён


def rnd_names():
    name = random.choice(names)
    return name

# Класс содержит в себе следующие параметры - название, процент защиты, атаку и жизнь
# Это могут быть предметы одежды, магические кольца, всё что угодно)


class Thing:
    def __init__(self, thing_name, thing_defense, thing_attack, thing_life):
        self.thing_name = thing_name
        self.thing_defense = thing_defense
        self.thing_attack = thing_attack
        self.thing_life = thing_life

# Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты. Параметры передаются через конструктор;
# а также методы для выполнения алгоритма, представленного ниже;


class Person:
    def __init__(self, pers_name, pers_health, pers_attack, pers_defense):
        self.pers_name = pers_name
        self.pers_health = pers_health
        self.pers_attack = pers_attack
        self.pers_defense = pers_defense

    # метод, принимающий на вход список вещей
    def set_things(self, things):
        pass

    # метод вычитания жизни на основе входной атаки
    def life_minus(self, attack_in):
        pass

# Класс наследуется от персонажа, при этом количество присвоенных жизней и процент защиты умножается на 2 в конструкторе


class Paladin(Person):
    def __init__(self, pers_name, pers_health, pers_attack, pers_defense):
        super().__init__(pers_name, pers_health, pers_attack, pers_defense)
        self.pers_health = pers_health * 2
        self.pers_defense = pers_defense * 2

# Класс наследуется от персонажа, при этом атака умножается на 2 в конструкторе


class Warrior(Person):
    def __init__(self, pers_name, pers_health, pers_attack, pers_defense):
        super().__init__(pers_name, pers_health, pers_attack, pers_defense)
        self.pers_attack = pers_attack * 2
