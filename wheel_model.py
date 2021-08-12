"""
Wheel game implementation.
"""

import pygame
import os.path
import random
from config import rig

class Screen:
    """
    """
    LENGTH = 650
    HEIGHT = 650
    BACKGROUND_COLOR = 'blue'
    WHEEL_LOCATION = (325,290)
    SPIN_BUTTON_LOCATION = (325,600)
    STARTUP_IMAGE_LOCATION = (325,325)
    ARROW_LOCATION = (325,40)
    RIG_DICT = {'double_points':(355, 320), 'minus_100':(310, 275), \
                'punishment':(265, 230), 'minus_50':(220, 185), \
                'plus_100':(175, 140), '1.5_multiplier':(130, 95), \
                '1.25_multiplier':(85, 50), '?':(40, 5), '':(360,0)}
    STARTUP_IMAGE_PATH = 'assets/images/startup_final.png'

    def  __init__(self):
        """
        """
        self._wheel_angle = 0
        self._light_on = False
        self._rotation_speed = 0
        self._start_game = False
        self._rig = rig
        self._rig_key = None
        pygame.mixer.init()
        self.BUTTON_CLICK_SOUND = \
            pygame.mixer.Sound('assets/sounds/click_sound.wav')
        self.WHEEL_CLICK_SOUND = \
            pygame.mixer.Sound('assets/sounds/wheel_click_sound.wav')
        self._new_game = False


def rotate_wheel(original_wheel, wheel_angle):
    """
    """
    return pygame.transform.rotate(original_wheel, wheel_angle)

def save_file(rotated_wheel, file_name):
    """
    """
    pygame.image.save(rotated_wheel, file_name)
    print('Creating ' + file_name)

def check_file(file_name):
    """
    """
    return os.path.isfile(file_name)

def validate_files(original_wheel):
    """
    """
    missing_files = 0
    for angle in range(0,361,1):
        wheel_path = 'assets/images/rotated_wheels/rotated_wheel_' + \
            str(angle) + '.png'
        if check_file(wheel_path) is False:
            missing_files += 1
            save_file(rotate_wheel(original_wheel, angle), wheel_path)
    print(f'All files validated. {str(missing_files)} files were missing!')

def generate_random_number(range=(361, 0)):
    random.seed()
    random_number = random.randrange(range[1],range[0],5)
    if random_number in [0,45,90,135,180,225,270,315,360]: # Reroll if random \
        # number falls in between prize options. 
        random_number = generate_random_number()
    return random_number

def divide_final_spin(angle, list=[]):
    if angle < 4:
        list.append(angle)
        return list
    elif angle % 5 != 0:
        list.append(angle % 5)
        angle = angle - (angle % 5)
    else:
        list.append(5)
        angle = angle - 5
    if angle == 0:
        return list
    return divide_final_spin(angle, list)


        


