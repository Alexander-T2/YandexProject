
level_map1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'X              X                  X',
    'X                                 X',
    'X                     X           X',
    'X                     X           X',
    'X                     X      X    X',
    'X               PD    XXX         X',
    'X               XX                X',
    'X                                 X',
    'X                                 X',
    'X                         K       X',
    'X           X           XXXXXXXXXXX',
    'X           X             X        ',
    'X                     S            ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map2 = [
    'X                                  ',
    '               X                   ',
    '                                   ',
    '                                   ',
    '                                   ',
    '                             X     ',
    '                      XXX          ',
    '                XX                 ',
    '                                   ',
    '                                   ',
    '                                   ',
    'X           X                     D',
    'X           X                     X',
    'X            XPX                  X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map3 = [
    'X                                  ',
    '               X                   ',
    '                                   ',
    '                                   ',
    '                                   ',
    '                             X     ',
    '                      XXX          ',
    '                XX                 ',
    '                                   ',
    '                                   ',
    '            XXXX  XXXXX            ',
    'X           X         X           D',
    'X           X         X           X',
    'X           X P     D X           X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

tile_size = 64
screen_width = 1800
current_level = 1
menu_state = 0
dead_state = 0
door_locked = 1
levels = {1: level_map1, 2: level_map2, 3: level_map3}
screen_height = len(levels[current_level]) * tile_size
