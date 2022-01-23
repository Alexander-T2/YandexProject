
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
    'X                                 X',
    'X           X           XXXXXXXXXXX',
    'X           X             X        ',
    'X                                  ',
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

tile_size = 64
screen_width = 1800
current_level = 1
levels = {1: level_map1, 2: level_map2}
screen_height = len(levels[current_level]) * tile_size
