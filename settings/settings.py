import pygame


level_map1 = [
    'X             XXXXX                         XXXXXXX                 XXX                   X',
    'X              XXX                           XXXXX                  XXX                   X',
    'X               X                             XXX                   XXXK                  X',
    'X                                              X                     X                    X',
    'X                                                                        X                X',
    'X                                                                           X             X',
    'X                                                                               X         X',
    'X                                                                                     XXXXX',
    'X                                                                                    X    X',
    'X                                                                                     D    ',
    'X                                                                                   XXXXXXX',
    'X                                                     P                            XXXXXXXX',
    'X                 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXX',
    'X                XX                                                  XX          XXXXXXXXXX',
    'X               XXXSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSXXX        XXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
]

level_map2 = [
    'XXXXXXXXX                                                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'X                                                                                                               X',
    'X                                                                                                               X',
    'X                                                                                                               X',
    'X                         S S       X    X                                                                      X',
    'X     P                   XXX XXX       XXX   X                                                                 X',
    'X  XXXXXXX   X        S    X   X                X                                                               X',
    'X       BX    X      XXX                         X                                                              X',
    'XXXXLLLLLXXX     X    X                            X   XX                              X                        X',
    'X          X                                                X                       X                           X',
    'X          X                                                   XX   X   X  X X X           XX                   X',
    'X          X                                                                          X        X   XX           X',
    'X          X                                                                                            XXXXXXXXX',
    'X  SDS     X                                                                                            L       X',
    'X  XXX                    S    S S S    SS      SSS        SS S                                         L   K   X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map3 = [
    'X                                                             s                                                   ',
    'X                                                                                                               X',
    '                                                                                                                 ',
    '                                                                                                                 ',
    '                                                                                                                 ',
    '                                                                                                                 ',
    '                                                                                                                 ',
    '                                                                                                                 ',
    '                                                                                                                 ',
    '                                                                                                                X',
    'X                                                                                                               X',
    'X                                                                                                               X',
    'X                   S   S                                                                                       D',
    'X                                                                                                               X',
    'X     S            PSSSSSD                             S                                                        X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
]

level_map4 = ['  ']

tile_size = 64
screen_width = 1800
current_level = 1
game_started = 0
menu_state = 0
dead_state = 0
door_locked = 1
menu_choose = 0
levels = {1: level_map1, 2: level_map2, 3: level_map3, 4: level_map4}
screen_height = 16 * tile_size

stories = {1: ["I have been talented and lucky.",
               "Some people even said I could pass through a locked door without opening the lock.",
               "But I never valued my gifts..."],
           2: ["With time, my overconfidence started biting me in my tail.",
               "Tasks didn't seem so easy and no one was as amazed as they used to be.",
               "I didn't understand how others struggled for what I took for granted..."],
           3: ["I grew desperate and began trying everything in order to save my position.",
               "Even such basic words like 'trust' and 'dignity' became something foreign to me.",
               "I was stepping over peoples heads.",
               "They must have felt awful..."],
           4: ""}
