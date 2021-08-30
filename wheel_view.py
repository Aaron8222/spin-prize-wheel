"""
View implementation.
"""
import pygame



def play_click_sound(click_sound):
    """
    Plays a button click sound.

    ARGS:
        click_sound: 

    RETURNS:
        None.
    """
    pygame.mixer.Sound.play(click_sound)

def play_wheel_click_sound(click_sound):
    """
    Plays a prize wheel rachet sound.

    ARGS:
        click_sound:

    RETURNS:
        None.
    """
    pygame.mixer.Sound.play(click_sound)


class View():
    """

    Attributes:
    """
    spin_button = pygame.image.load('assets/images/spin_button_final.png')
    blank_wheel = pygame.image.load('assets/images/wheel_blank.png')
    wheel = pygame.image.load('assets/images/wheel_original.png')
    arrow = pygame.image.load('assets/images/arrow_final.png')

    def __init__(self, screen):
        """
        """
        self._screen = screen
        self._display = \
            pygame.display.set_mode((self._screen.LENGTH,self._screen.HEIGHT))
        self._rot_wheel = None
        self._spin_button_rect = \
            self.spin_button.get_rect(center=self._screen.SPIN_BUTTON_LOCATION)
        self._arrow_rect = \
            self.arrow.get_rect(center=self._screen.ARROW_LOCATION)
        self._startup = pygame.image.load(self._screen.STARTUP_IMAGE_PATH)
        self._final_wheel = None


    def start_draw(self):
        """
        """
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Ultimate Spin Wheel")
        clock = pygame.time.Clock()
        clock.tick(60)
        icon = pygame.image.load(self._screen.STARTUP_IMAGE_PATH)
        pygame.display.set_icon(icon)
        self._display.fill('white')
        self.draw_startup()
        pygame.display.update()

    def main_draw(self, rotated_wheel_dict):
        """
        """
        self._display.fill(self._screen.BACKGROUND_COLOR)
        self.draw_wheel(rotated_wheel_dict)
        if self._screen._start_game is True:
            if self._screen._wheel_angle % 30 == 0:
                play_wheel_click_sound(self._screen.WHEEL_CLICK_SOUND)
        self.draw_spin_button()
        self.draw_arrow()
        pygame.display.update()

    def draw_wheel(self, rotated_wheel_dict):
        """
        """
        self._rot_wheel = rotated_wheel_dict['rotated_wheel_' + \
            str(360 + self._screen._wheel_angle)] # Find complement
        wheel_rect = \
            self._rot_wheel.get_rect(center=self._screen.WHEEL_LOCATION)
        self._display.blit(self._rot_wheel, wheel_rect)
        
    def draw_spin_button(self):
        """
        """
        self._display.blit(self.spin_button, self._spin_button_rect)

    def draw_arrow(self):
        """
        """
        self._display.blit(self.arrow, self._arrow_rect)

    def draw_startup(self):
        """
        """
        startup_rect = \
            self._startup.get_rect(center=self._screen.STARTUP_IMAGE_LOCATION)
        self._display.blit(self._startup, startup_rect)


def load_wheel_image():
    """
    Loads and caches all rotated wheels.

    ARGS:
        None.

    RETURNS:
        None.
    """
    rotated_wheel_dict = {}
    for angle in range(0,361,1):
        wheel_path = 'assets/images/rotated_wheels/rotated_wheel_' + \
            str(angle) + '.PNG'
        rotated_wheel_dict['rotated_wheel_{0}'.format(angle)] = \
            pygame.image.load(wheel_path)
    print('All files loaded!')
    return rotated_wheel_dict

