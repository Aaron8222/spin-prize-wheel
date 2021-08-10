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

def get_rig_key():
    """
    Gets the rig key to determine which prize to give.

    ARGS:
        None.

    RETURNS:
        A string representing the key for which prize to give.
    """
    return input('Enter key: ')