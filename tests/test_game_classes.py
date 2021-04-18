import pytest
from game_classes import Person, Thing, Inventory


PROTECTION = 0.1
HP = 100
SIZE_INVENTORY = 5


@pytest.fixture
def person() -> Person:
    person = Person(
        name="Тестер", hit_points=HP, protection=PROTECTION, attack_damage=40
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
    def test_add_thing(self, inventory: Inventory, sword: Thing):
        inventory.add_thing(sword)
        assert inventory.things[0] == sword

    def test_overflow(self, inventory: Inventory, sword: Thing):
        SIZE_INVENTORY = 5
        for _ in range(SIZE_INVENTORY):
            inventory.add_thing(sword)

        assert not inventory.add_thing(sword), "инвентарь не переполнился"


class TestPerson:
    def test_reduce_hit_points(self, person: Person) -> None:
        damage = 50
        person.reduce_hit_points(damage)
        exept_hp = HP - damage * (1 - PROTECTION)
        assert person.current_hit_points == exept_hp
