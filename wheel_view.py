"""
View implementation.
"""
import pygame



def play_click_sound():
    """
    Plays a click sound
    """
    click_sound = pygame.mixer.Sound('assets/sounds/click_sound.wav')
    pygame.mixer.Sound.play(click_sound)

class View():
    """

    Attributes:
    """
    spin_button = pygame.image.load('assets/images/spin_button_final.png')
    wheel = pygame.image.load('assets/images/wheel_final.png')
    

    def __init__(self, screen):
        """
        """

        self._screen = screen
        self._display = pygame.display.set_mode((self._screen.LENGTH,self._screen.HEIGHT))
        self._rot_wheel = pygame.transform.rotate(self.wheel,self._screen._wheel_angle)

    def main_draw():
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Ultimate Spin Wheel")

        # icon = pygame.image.load('')
        # pygame.display.set_icon(icon)

        self._display.fill(self._screen.BACKGROUND_COLOR)

        self.draw_wheel()
        self.draw_spin_button()


        pygame.display.update()

    def draw_wheel():
        wheel_image = pygame.image.load(self._rot_wheel).convert_alpha()
        wheel_rect = wheel_image.get_rect()
        wheel_rect.x = self._screen.WHEEL_LOCATION[0]
        wheel_rect.y = self._screen.WHEEL_LOCATION[1]
        self._display.blit(wheel_image, wheel_rect)

    def draw_spin_button():
        spin_button_image = pygame.image.load(self.spin_button).convert_alpha()
        spin_button_rect = spin_button_image.get_rect()
        spin_button_rect.x = self._screen.SPIN_BUTTON_LOCATION[0]
        spin_button_rect.y = self._screen.SPIN_BUTOON_LOCATION[1]
        self._display.blit(spin_button_image, spin_button_rect)

