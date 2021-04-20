import pytest
from game_classes import Person, Thing, Inventory, InventoryOverflowError


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
    def test_reduce_hit_points(self, person: Person) -> None:
        damage = 50
        person.reduce_hit_points(damage)
        exept_hp = HP - damage * (1 - person.protection)
        assert person.current_hit_points == exept_hp

    def test_take_thing(self, person: Person) -> None:
        sword = Thing(
            name="Мечь",
            multiplier_hit_points=0.1,
            protection=0.1,
            attack_damage=10,
        )
        for _ in range(len(person.inventory)):
            assert person.inventory.append(
                sword
            ), "Преждевременно переполнение инвентаря"

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
        person.take_thing(ring_of_health)
        exept_final_hp = person.hit_points * (
            1 + ring_of_health.multiplier_hit_points
        )
        assert (
            person.final_hit_points == exept_final_hp
        ), "Показатель здоровья не увеличился"
