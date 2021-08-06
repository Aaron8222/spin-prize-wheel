"""
Wheel game implementation.
"""

import pygame
import os.path

class Screen:
    """
    """
    LENGTH = 650
    HEIGHT = 650
    BACKGROUND_COLOR = 'blue'
    WHEEL_LOCATION = (325,290)
    SPIN_BUTTON_LOCATION = (325,480)
    RIG = 0 # Angle at which you want to land on
   


    def  __init__(self):
        """
        """
        self._wheel_angle = 0
        self._light_on = False
        self._rotation_speed = 0
        self._start_game = False


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
    for angle in range(0,361):
        wheel_path = 'assets/images/rotated_wheels/rotated_wheel_' + str(angle) + '.png'
        if check_file(wheel_path) is False:
            missing_files += 1
            save_file(rotate_wheel(original_wheel, angle), wheel_path)
    print('All files validated. ' + str(missing_files) + ' files were missing!')
        


