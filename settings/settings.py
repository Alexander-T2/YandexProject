
level_map1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'X                                                                                                               X',
    'X                                                                                                               X',
    'X                                                                                                               X',
    'X                     X                                                                                         X',
    'X                     X      X                                                                          X        ',
    'X    P   D                  S                                                                                   X',
    'X                     XXX                                                                                       X',
    'X               XX                                                                                              X',
    'X                                                                                                               X',
    'X                                                                                                               X',
    'X                                                                                                               X',
    'X           X                                                                                         XXXXXXXXXXX',
    'X           X                                                                                           X        ',
    'X    P   D                  S                                                                                    ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX '
]

level_map2 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'X                                                                                                               X',
    'X                   X                                                                                           X',
    'X                                                                                                               X',
    'X                                                                                                               X',
    'X                                                                                                               X',
    'X                                                                                                          X    X',
    'X                          XXX                                                                                  X',
    'X                    XX                                                                                         X',
    'X                                                                                                               X',
    'X                                                                                                               X',
    'X                                                                                                               X',
    'X                X                                                                                              X',
    'X                X   KD                                                                                         X',
    'X                 XPX                                                                                           X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map3 = [
    'X                                                                                                                ',
    'X                                                                                                               X',
    '                    X                                                                                            ',
    '                                                                                                                 ',
    '                                                                                                                 ',
    '                                                                                                                 ',
    '                                  X                                                                              ',
    '                           XXX                                                                                   ',
    '                     XX                                                                                          ',
    '                                                                                                                X',
    'X                                                                                                               X',
    'X                XXXX  XXXXX                                                                                    X',
    'X                X         X                                                                                    D',
    'X                X         X                                                                                    X',
    'X                X P  K  D X                                                                                    X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
]
extra_map = [None for i in range(16)]


tile_size = 64
screen_width = 1800
current_level = 1
game_started = 0
menu_state = 0
dead_state = 0
door_locked = 1
menu_choose = 0
levels = {1: level_map1, 2: level_map2, 3: level_map3}
screen_height = 16 * tile_size
