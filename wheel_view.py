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
    #scaled_wheel = pygame.transform.scale(wheel,(500,500))
    #scaled_spin_button = pygame.transform.scale(spin_button,(300,100))


    def __init__(self, screen):
        """
        """

        self._screen = screen
        self._display = pygame.display.set_mode((self._screen.LENGTH,self._screen.HEIGHT))
        self._rot_wheel = pygame.transform.rotate(self.wheel,self._screen._wheel_angle)
        self._spin_button_rect = self.spin_button.get_rect(center=self._screen.SPIN_BUTTON_LOCATION)
        # self._surface = pygame.Surface((2500,2500))

    def main_draw(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Ultimate Spin Wheel")

        # icon = pygame.image.load('')
        # pygame.display.set_icon(icon)

        self._display.fill(self._screen.BACKGROUND_COLOR)
        self.draw_wheel()
        self.draw_spin_button()
        # surface2 = pygame.transform.smoothscale(self._surface,self._display.get_rect().size)
        # self._display.blit(surface2,(0,0))
        pygame.display.update()

    def draw_wheel(self):
        self._rot_wheel = pygame.transform.rotate(self._rot_wheel,self._screen._wheel_angle)
        wheel_rect = self._rot_wheel.get_rect(center=self._screen.WHEEL_LOCATION)
        self._display.blit(self._rot_wheel, wheel_rect)
        #self._surface.blit(self._rot_wheel, wheel_rect)

    def draw_spin_button(self):
        #self._surface.blit(self.spin_button, self._spin_button_rect)
        self._display.blit(self.spin_button, self._spin_button_rect)

