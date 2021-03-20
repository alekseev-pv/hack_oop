import random
from typing import List, Union

from colorama import Back, Fore, Style

from persons import CatDog, Paladin, Person, Warrior
from random_generation_utils import RandomGenerationUtils as randomGeneration
from things import Things

PersonsList = List[Union[Person, Paladin, Warrior, CatDog]]


class Arena:
    number_of_fighters = 10
    things: List[Things]
    persons: PersonsList

    def __init__(self):
        self.create_things()
        self.create_persons()

    def create_things(self) -> List[Things]:
        """
        Шаг 1 - создаем произвольное количество вещей с различными параметрами,
         процент защиты не должен превышать 10%(0.1).
         Сортируем по проценту защиты, по возрастанию;
        """

        amount = random.randint(4, 20)

        arena_things: List[Things] = []
        for n in range(amount):
            arena_things.append(randomGeneration.get_random_thing())

        self.things = sorted(arena_things,
                             key=lambda this_thing: this_thing.per_protection)

        print(Back.LIGHTBLACK_EX + 'Создали вещи:' + Style.RESET_ALL)
        for thing in self.things:
            print(thing.__dict__)
        return self.things

    def create_persons(self) -> PersonsList:
        """
        Шаг 2 - создаем произвольно 10 персонажей, кол-во воинов и паладинов
         произвольно.
        Придумайте своих уникальных персонажей или заставьте сражаться
         знаменитостей, посмотрим кто сильнее =)
        """

        persons_names = randomGeneration.get_random_person_names_list(
            self.number_of_fighters)
        persons_list: PersonsList = []
        for person_name in persons_names:
            person_type = randomGeneration.get_random_person_type()
            life_counter, base_attack, base_protection = (
                randomGeneration.get_random_person_params())
            persons_list.append(globals()[person_type](
                name=person_name, life_counter=life_counter,
                base_attack=base_attack, base_protection=base_protection))

        print(Back.LIGHTBLACK_EX + f'Создали {len(persons_list)} персонажей'
              + Style.RESET_ALL)

        self.persons = persons_list
        return self.persons

    def put_on_things(self) -> PersonsList:
        """
        Шаг 3 - одеваем персонажей рандомными вещами.
        Кому-то 1, кому-то больше, но не более 4 вещей в одни руки;
        Вещи из списка things_list могут повторяться у разных персонажей
        """

        for person in self.persons:
            number_of_things = random.randint(1, 4)
            person.set_things(random.sample(self.things, number_of_things))

        for person in self.persons:
            print(person.__dict__)
        return self.persons

    def attack(self) -> PersonsList:
        """
        Одна атака.
        Выбирается пара Нападающий и Защищающийся.

        Как только кол-во жизней меньше или равно 0,
        персонаж удаляется из арены (списка).

        Для отслеживания процесса битвы выведите информацию в таком виде:
        {атакующий персонаж} наносит удар по {защищающийся персонаж} на
        {кол-во урона} урона
        """

        attacking: Person
        defending: Person
        attacking, defending = random.sample(self.persons, 2)

        damage = round(defending.decrease_life(attacking), 2)

        print(Fore.MAGENTA + f'\n{attacking.name} '
              + Style.RESET_ALL + 'наносит удар по '
              + Fore.CYAN + f'{defending.name} '
              + Style.RESET_ALL + 'на '
              + Fore.MAGENTA + f'{damage} урона' + Style.RESET_ALL)
        print(Fore.CYAN
              + f'У {defending.name} осталось {defending.all_life} жизни'
              + Style.RESET_ALL)

        if defending.all_life <= 0:
            self.persons.remove(defending)

        return self.persons

    def arena_fighting(self):
        """
        Шаг 4 - отправляем персонажей на арену.
        Цикл идет до тех пор, пока не останется последнего выжившего.
        """

        while len(self.persons) > 1:
            self.attack()

    @staticmethod
    def print_winner(winner: Person):
        """
        Вывести победителя
        """

        print('\n'
              + Back.LIGHTYELLOW_EX + Fore.BLACK + Style.BRIGHT
              + f'Winner is: {winner.name}'
              + Style.RESET_ALL)

    def arena_game(self):
        """
        Вызов процесса игры.
        1, 2 Генерация списка вещей и персонажей - в конструкторе класса
        Сделать шаги:
        3. Надеваем вещи - put_on_things()
        4. Отправляем персонажей на арену - arena_fighting()
        5. Выводим победителя
        """

        self.put_on_things()
        self.arena_fighting()
        winner = self.persons[0]
        self.print_winner(winner)


battle = Arena()
battle.arena_game()
