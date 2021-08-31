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

def get_rig_key(option_list, options_dict):
    """
    Gets the rig key to determine which prize to give.

    ARGS:
        None.

    RETURNS:
        A string representing the key for which prize to give.
    """
    key = input('Enter key: ')
    if key not in option_list:
        key = get_rig_key(option_list, options_dict)
    print(f'Success! You may spin the wheel!')
    return options_dict[key]
