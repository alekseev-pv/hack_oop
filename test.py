import unittest
from things import Thing
from persons import Paladin, Warrior, Person, Goblin, Elf
from arena import Arena


class TestThings(unittest.TestCase):
    def setUp(self) -> None:
        self.thing = Thing('ring', 10, 10, 10)

    def test_defense_percentage(self):
        self.thing.defense = 10
        self.assertEqual(self.thing.defense_percentage, 0.1)
        self.thing.defense = 0.02
        self.assertEqual(self.thing.defense_percentage, 0.02)


class TestCreatePerson(unittest.TestCase):

    def setUp(self):
        self.thing = Thing('ring', 10, 10, 10)
        self.paladin = Paladin('paladin', 10, 10, 10)
        self.warrior = Warrior('warrior', 10, 10, 10)
        self.person = Person('person', 10, 10, 10)
        self.goblin = Goblin('goblin', 10, 10, 10)
        self.elf = Elf('elf', 10, 10, 10)


    def test_create_paladin(self):
        self.assertEqual(self.paladin.hit_points, 20)
        self.assertEqual(self.paladin.defense, 20)

    def test_create_warrior(self):
        self.assertEqual(self.warrior.attack_damage, 20)

    def test_create_elf(self):
        self.assertEqual(self.elf.hit_points, 11.0)
        self.assertEqual(self.elf.defense, 12.0)
        self.assertEqual(self.elf.attack_damage, 25)

    def test_create_goblin(self):
        self.assertEqual(self.goblin.hit_points, 30)
        self.assertEqual(self.goblin.defense, 20)
        self.assertEqual(self.goblin.attack_damage, 9.0)

    def test_is_alive(self):
        self.person.hit_points = 0
        self.assertEqual(self.person.is_alive, False)
        self.person.hit_points = 10
        self.assertEqual(self.person.is_alive, True)

    def test_attack(self):
        self.person.update_hp_after_attack(self.paladin)
        self.assertEqual(self.person.hit_points, 1.0)

    def test_add_thing(self):
        self.person.set_things((self.thing,))
        self.assertEqual(self.person.hit_points, 20)
        self.assertEqual(self.person.attack_damage, 20)
        self.assertEqual(self.person.defense, 11)
        self.assertIn(self.thing, self.person.things)


class TestArena(unittest.TestCase):
    def setUp(self) -> None:
        self.name_thing = {}
        self.name_persons = ('Oleg', 'Anna')
        self.arena = Arena('Колизей')

    def test_create_persons(self):
        self.arena.create_persons(self.name_persons, count=2)
        self.assertEqual(len(self.arena.get_persons()), 2)

    def test_battle(self):
        warrior_1 = Warrior('warrior_1', 10, 10, 10)
        warrior_2 = Warrior('warrior_2', 200, 200, 200)
        arena = Arena('Test')
        arena._persons += [warrior_1, warrior_2]
        arena.battle()
        self.assertEqual(len(arena.get_persons()), 1)
        self.assertEqual(arena.get_persons()[0].name, 'warrior_2')


if __name__ == '__main__':
    unittest.main()
