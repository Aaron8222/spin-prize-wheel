"""
View implementation.
"""
import pygame



def play_click_sound(click_sound):
    """
    Plays a click sound
    """
    pygame.mixer.Sound.play(click_sound)

def play_wheel_click_sound(click_sound):
    """
    Plays a click sound
    """
    pygame.mixer.Sound.play(click_sound)

class View():
    """

    Attributes:
    """
    spin_button = pygame.image.load('assets/images/spin_button_final.png')
    wheel = pygame.image.load('assets/images/wheel_final.png')
    arrow = pygame.image.load('assets/images/arrow_final.png')
    #scaled_wheel = pygame.transform.scale(wheel,(500,500))
    #scaled_spin_button = pygame.transform.scale(spin_button,(300,100))


    def __init__(self, screen):
        """
        """

        self._screen = screen
        self._display = pygame.display.set_mode((self._screen.LENGTH,self._screen.HEIGHT))
        self._rot_wheel = None
        self._spin_button_rect = self.spin_button.get_rect(center=self._screen.SPIN_BUTTON_LOCATION)
        self._arrow_rect = self.arrow.get_rect(center=self._screen.ARROW_LOCATION)
        # self._surface = pygame.Surface((2500,2500))


    def main_draw(self, rotated_wheel_dict):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Ultimate Spin Wheel")
        clock = pygame.time.Clock()
        clock.tick(60)
        # icon = pygame.image.load('')
        # pygame.display.set_icon(icon)

        self._display.fill(self._screen.BACKGROUND_COLOR)
        self.draw_wheel(rotated_wheel_dict)
        # self.draw_wheel()
        self.draw_spin_button()
        self.draw_arrow()
        # surface2 = pygame.transform.smoothscale(self._surface,self._display.get_rect().size)
        # self._display.blit(surface2,(0,0))
        pygame.display.update()


    def draw_wheel(self, rotated_wheel_dict):
        self._rot_wheel = rotated_wheel_dict['rotated_wheel_' + str(360+self._screen._wheel_angle)]
        # wheel_path = 'assets/images/rotated_wheels/rotated_wheel_' + str(360+self._screen._wheel_angle) + '.PNG'
        # print(wheel_path)
        # self._rot_wheel = pygame.image.load(wheel_path)
        wheel_rect = self._rot_wheel.get_rect(center=self._screen.WHEEL_LOCATION)
        self._display.blit(self._rot_wheel, wheel_rect)
        #self._surface.blit(self._rot_wheel, wheel_rect)
        # play_wheel_click_sound(self._screen.WHEEL_CLICK_SOUND)
        

    def draw_spin_button(self):
        #self._surface.blit(self.spin_button, self._spin_button_rect)
        self._display.blit(self.spin_button, self._spin_button_rect)

    def draw_arrow(self):
        self._display.blit(self.arrow, self._arrow_rect)

def load_wheel_image():
    """
    """
    rotated_wheel_dict = {}
    for angle in range(0,361,1):
        wheel_path = 'assets/images/rotated_wheels/rotated_wheel_' + str(angle) + '.PNG'
        rotated_wheel_dict['rotated_wheel_{0}'.format(angle)] = pygame.image.load(wheel_path)
    print('All files loaded!')
    return rotated_wheel_dict

