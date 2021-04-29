import pytest
from package.game_classes import (
    Person,
    Warrior,
    Paladin,
    Thing,
    Inventory
)
from package.errors import InventoryOverflowError


PROTECTION = 0.1
HP = 100
SIZE_INVENTORY = 5


@pytest.fixture
def person() -> Person:
    person = Person(
        name="Тестер", hit_points=HP, protection=0, attack_damage=40
    )
    return person


@pytest.fixture
def sword() -> Thing:
    sword = Thing(
        name="Мечь",
        multiplier_hit_points=0.1,
        protection=PROTECTION,
        attack_damage=10,
    )
    return sword


@pytest.fixture
def inventory() -> Inventory:
    inventory = Inventory(SIZE_INVENTORY)
    return inventory


class TestInventory:
    def test_append(self, inventory: Inventory, sword: Thing):
        inventory.append(sword)
        assert inventory.things[0] == sword

    def test_overflow(self, inventory: Inventory, sword: Thing):
        SIZE_INVENTORY = 5
        for _ in range(SIZE_INVENTORY):
            inventory.append(sword)

        try:
            inventory.append(sword)
            assert False, "инвентарь не переполнился"
        except InventoryOverflowError:
            pass


class TestPerson:
    def test_take_thing(self, person: Person, sword: Thing) -> None:
        for _ in range(len(person.inventory)):
            assert person.inventory.append(
                sword
            ), "Преждевременно переполнение инвентаря"

    def test_drop_thing(self, person: Person) -> None:
        sword = Thing(
            name="Мечь",
            multiplier_hit_points=0,
            protection=0,
            attack_damage=10,
        )
        ring = Thing(
            name="Кольцо",
            multiplier_hit_points=0.3,
            protection=0,
            attack_damage=0,
        )
        shield = Thing(
            name="Щит",
            multiplier_hit_points=0,
            protection=0.2,
            attack_damage=0,
        )
        person.take_thing(sword)
        person.take_thing(ring)
        person.take_thing(shield)

        person.drop_thing(thing=ring)
        assert person.inventory[0] == sword and person.inventory[1] == shield

        person.drop_thing(index=0)
        assert person.inventory[0] == shield

    def test_inventory_overflow(self, person: Person) -> None:
        sword = Thing(
            name="Мечь",
            multiplier_hit_points=0.1,
            protection=0.1,
            attack_damage=10,
        )
        for _ in range(len(person.inventory)):
            person.inventory.append(sword)

        assert not person.inventory.append(
            sword
        ), "Не произошло переполнения инвентаря"

    def test__update_protection(self, person: Person) -> None:
        shield = Thing(
            name="Щита",
            protection=0.1,
        )
        person.take_thing(shield)
        assert (
            person.final_protection == shield.protection
        ), "Показатель брони не увеличился"

    def test__update_attack_damage(self, person: Person) -> None:
        sword = Thing(
            name="Мечь",
            attack_damage=10,
        )
        person.take_thing(sword)
        assert (
            person.final_attack_damage
            == person.attack_damage + sword.attack_damage
        ), "Показатель атаки не увеличился"

    def test__update_hit_points(self, person: Person) -> None:
        ring_of_health = Thing(
            name="Кольцо здоровья",
            multiplier_hit_points=0.5,
        )
        person.current_hit_points = 50
        exept_current_hp = person.current_hit_points * (
            1 + ring_of_health.multiplier_hit_points
        )
        person.take_thing(ring_of_health)
        exept_final_hp = person.hit_points * (
            1 + ring_of_health.multiplier_hit_points
        )

        assert (
            person.final_hit_points == exept_final_hp
        ), "Показатель здоровья не увеличился"
        assert (
            person.current_hit_points == exept_current_hp
        ), "Текущее здоровье не увеличилось"

    def test_attack_damage(self, person: Person) -> None:
        attacker = Person(
            name="Атакующий", hit_points=100, protection=0, attack_damage=100
        )

        defender = Person(
            name="Атакующий", hit_points=100, protection=0.5, attack_damage=0
        )
        expect_hp = (
            defender.current_hit_points
            - defender.final_protection * attacker.final_attack_damage
        )
        attacker.attack(defender)

        assert (
            defender.current_hit_points == expect_hp
        ), "Неверный расчёт дамага"


class TestWarrior:
    attack = 100
    warrior = Warrior(
        name="Воин", hit_points=100, protection=0.1, attack_damage=attack
    )
    assert warrior.attack_damage == attack * 2


class TestPaladin:
    protection = 0.1
    hit_points = 100
    paladin = Paladin(
        name="Воин",
        hit_points=hit_points,
        protection=protection,
        attack_damage=1,
    )
    assert paladin.hit_points == hit_points * 2
    assert paladin.protection == protection * 2
