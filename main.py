import random
from typing import List

from rich.console import Console

from characters import Person, Thing

console = Console()


class Game:
    """Class for playing game."""

    game_things = []
    game_players = []
    player_classes = Person.__subclasses__()

    def create_players(self, players_names_list: List[str]) -> None:
        """Create players with random class and charecteristics.
        Takes created list of names.
        """
        for name in random.sample(players_names_list, 10):
            random_base_deffend = round(random.uniform(0, 0.3), 2)
            random_hp = random.randint(1, 100)
            random_base_attack = random.randint(1, 30)
            random_class = random.choice(self.player_classes)
            fighter = random_class(
                name, random_hp, random_base_attack, random_base_deffend
            )
            self.game_players.append(fighter)

    def create_random_things(self, LIST_THINGS_NAMES: List[str]) -> None:
        """Create things with random charecteristics.
        Takes created list of names.
        """
        for name in LIST_THINGS_NAMES:
            random_per_proc = round(random.uniform(0, 0.1), 2)
            random_hp = random.randint(1, 5)
            random_thing_attack = random.randint(1, 7)
            thing = Thing(
                name, random_per_proc, random_thing_attack, random_hp
            )
            self.game_things.append(thing)
        self.game_things.sort(key=lambda x: x.per_proc)

    def set_thing_on_players(self) -> None:
        """Take random (from 1 to 4) things and set on random player.
        Shuffle list of players and things before set for more justice.
        """
        random.shuffle(self.game_players)
        random.shuffle(self.game_things)
        for player in self.game_players:
            if self.game_things:
                try:
                    random_things_for_player = random.sample(
                        self.game_things, random.randint(1, 4)
                    )
                except ValueError:
                    random_things_for_player = random.sample(
                        self.game_things,
                        random.randint(1, len(self.game_things)),
                    )
                player.setThings(random_things_for_player)
                for thing in random_things_for_player:
                    self.game_things.remove(thing)
            else:
                console.print("Вещи розданы")
                break

    def start_game(self) -> None:
        """Start gaming with print in consile with rich" """
        live_players = self.game_players.copy()
        rounds = 0
        while len(live_players) > 1:
            rounds += 1
            console.print()
            console.print(f"[black on white bold underline]Раунд: {rounds}[/]")
            random_fighters = random.sample(live_players, 2)
            damage = random_fighters[0].calculate_hp_attack(random_fighters[1])
            console.print(
                f"[white on dark_red]{random_fighters[1].name}[/]"
                " наносит удар по "
                f"[bright_black on pale_green3]{random_fighters[0].name}[/]"
                f" на [underline]{damage}[/] урона"
            )
            console.print(
                f"У {random_fighters[0].name} осталось "
                f"[underline]{random_fighters[0].current_hp}[/] "
                "[dark_cyan]HP[/] "
            )
            if random_fighters[0].current_hp == 0:
                console.print(
                    f"{random_fighters[0].name} [bold red]УБИТ![bold red]"
                )
                live_players.remove(random_fighters[0])
        console.print()
        console.print(
            "ПОБЕДИТЕЛЬ :smiley: [underline green strike]"
            f"{live_players[0].name}[/] :smiley:"
        )


LIST_THINGS_NAMES = [
    "RING",
    "CLOAK",
    "HAT",
    "SWORD",
    "MEGA_SWORD",
    "SPEAR",
    "BFG",
    "Imperator's Spear",
]
LIST_PLAYERS_NAMES = [
    "Horus",
    "Leman Russ ",
    "Ferrus Manus",
    "Fulgrim",
    "Vulkan",
    "Rogal Dorn",
    "Roboute Guilliman",
    "Magnus the Red",
    "Sanguinius",
    "Lion El'Jonson",
    "Perturabo",
    "Mortarion",
    "Lorgar",
    "Jaghatai Khan",
    "Konrad Curze",
    "Angron",
    "Corvus Corax",
    "Alpharius Omegon",
    "Unknown and Forbidden II",
    "Unknown and Forbidden XI",
]

if __name__ == "__main__":
    game1 = Game()
    game1.create_random_things(LIST_THINGS_NAMES)
    game1.create_players(LIST_PLAYERS_NAMES)
    game1.set_thing_on_players()
    game1.start_game()
