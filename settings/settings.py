
level_map1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'X                                      X',
    'X                                      X',
    'X                                      X',
    'X                     X                X',
    'X                     X      X         X',
    'X                D    XXX              X',
    'X               XX                     X',
    'X                                      X',
    'X                                      X',
    'X                         K            X',
    'X           X                XXXXXXXXXXX',
    'X           X                  X        ',
    'XP                         S            ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map2 = [
    'X                                       ',
    '                    X                   ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                  X     ',
    '                           XXX          ',
    '                     XX                 ',
    '                                        ',
    '                                        ',
    '                                        ',
    'X                X                    KD',
    'X                X                     X',
    'X                 XPX                  X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map3 = [
    'X                                       ',
    '                    X                   ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                  X     ',
    '                           XXX          ',
    '                     XX                 ',
    '                                        ',
    '                                        ',
    '                 XXXX  XXXXX            ',
    'X                X         X           D',
    'X                X         X           X',
    'X                X P  K  D X           X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

tile_size = 64
screen_width = 1800
current_level = 1
menu_state = 0
dead_state = 0
door_locked = 1
menu_choose = 0
levels = {1: level_map1, 2: level_map2, 3: level_map3}
screen_height = len(levels[current_level]) * tile_size
