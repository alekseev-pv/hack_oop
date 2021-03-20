import colorama

from battles import Battle

MAX_PLAYERS_COUNT = 2


def main():
    colorama.init()
    while True:
        if input('Новая битва? y/n:') == 'y':
            print(colorama.Fore.RED + 'Да начнется битва!')
            print(colorama.Style.RESET_ALL)
            battle = Battle()
            battle.fill_things()
            battle.fill_persons()

            if input('Раздать вещи? y/n:') == 'y':
                battle.choose_things()
            else:
                print('Будем биться голыми руками. Ок.')
            print('Участники битвы:')
            for player in battle.players:
                print(player)

            input('Нажми Ввод, продолжить')

            players_count = MAX_PLAYERS_COUNT
            while len(battle.players) > 1:
                battle.choose_players(players_count)
                print('\nНа арене:')
                for player in battle.players_on_arena:
                    print(player)
                print()
                input('Нажми ввод, чтобы начать')
                battle.fight()
                battle.return_players()
                players_count = min(len(battle.players),
                                    players_count)

            print()
            print(colorama.Fore.RED + 'Победитель:')
            for player in battle.players:
                print(player.name)
            print(colorama.Style.RESET_ALL)

        else:
            break


if __name__ == '__main__':
    main()
