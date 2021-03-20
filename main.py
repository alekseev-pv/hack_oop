import Classes

number_of_bots = 20
number_of_things = 40

arena = Classes.Arena()
list_of_participants = arena.create_bots_with_things(number_of_things,
                                                     number_of_bots)
arena.bots_battle(list_of_participants)
