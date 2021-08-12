import pygame


def get_mouse_position():
    """
    Determines current mouse cursor position.

    ARGS:
        None.

    RETURNS:
        A tuple representing position of the mouse.
    """
    return pygame.mouse.get_pos()

def get_rig_key(dict):
    """
    Gets the rig key to determine which prize to give.

    ARGS:
        None.

    RETURNS:
        A string representing the key for which prize to give.
    """
    key = input('Enter key: ')
    if key not in dict.keys():
        print(f'{key} is an invalid key! Please choose from the following:\n'
        'Double Points: double_points\n'
        '-100 Points: minus_100\n'
        'Punishment: punishment\n'
        '-50 Points: minus_50\n'
        '+100 Points plus_100\n'
        '1.5x Multiplier: 1.5_multiplier\n'
        '1.25x Multiplier: 1.25_multiplier\n'
        '?: ?\n'
        'Random: Leave Blank')
        key = get_rig_key(dict)
    print(f'Success! You may spin the wheel!')
    return key
