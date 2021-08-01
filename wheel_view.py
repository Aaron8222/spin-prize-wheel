"""
View implementation.
"""
import pygame
from wheel_controller import 


def play_click_sound():
    """
    Plays a click sound
    """
    click_sound = pygame.mixer.Sound('sounds/click_sound.wav')
    pygame.mixer.Sound.play(click_sound)

class View():
    """

    Attributes:
    """
    spin_button = pygame.image.load('')
    

    def __init__(self, screen):
        """
        """

        self._screen = screen
        self._display = pygame.display.set_mode((_screen.LENGTH,_screen.HEIGHT))
        self._wheel = pygame.image.load('')