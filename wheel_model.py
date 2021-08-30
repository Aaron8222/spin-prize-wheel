"""
Wheel game implementation.
"""

from math import sqrt
import pygame
import os.path
import random
from config import rig, options
import shelve

class Screen:
    """
    """
    LENGTH = 650
    HEIGHT = 650
    BACKGROUND_COLOR = 'blue'
    WHEEL_LOCATION = (325,300)
    SPIN_BUTTON_LOCATION = (325,600)
    STARTUP_IMAGE_LOCATION = (325,325)
    ARROW_LOCATION = (325,40)
    RIG_DICT = {'option_1': (0, 45), 'option_2': (45, 90), \
                'option_3': (90, 135), 'option_4': (135, 180), \
                'option_5': (180, 225), 'option_6': (225, 270), \
                'option_7': (270, 315), 'option_8': (315, 360), '': (0,360)}
    STARTUP_IMAGE_PATH = 'assets/images/startup_final.png'
    OPTIONS_DICT = {}

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

def draw_text(text, rotate_angle): # For creating/caching images with the wheel
    # ADD all text here??
    font = pygame.font.SysFont(None, 24)
    img = font.render(text, True, (0, 0, 0))
    return pygame.transform.rotate(img, rotate_angle)

def save_file(rotated_wheel, file_name):
    """
    """
    pygame.image.save(rotated_wheel, file_name)
    print('Creating ' + file_name)

def check_file(file_name):
    """
    """
    return os.path.isfile(file_name)

def create_wheel(blank_wheel, length, height, options_dict):
    surface = \
        pygame.Surface([length, height], pygame.SRCALPHA)
    wheel_rect = blank_wheel.get_rect(center=(length/2, height/2))
    surface.blit(blank_wheel, wheel_rect)
    option_locations = find_text_location()
    for text_number in range(1,9):
        # option_locations = {1:(459, 277.5),2:(373,459),3:(277,459),4:(191,373),5:(191, 277),6:(277, 191),7:(373, 191),8:(459, 373)}
        option = options_dict[f'option_{text_number}']
        rotated_text = draw_text(option[0],option[1])
        rotated_text_rect = rotated_text.get_rect(center=option_locations[text_number])
        surface.blit(rotated_text, rotated_text_rect)
    save_file(surface, 'assets/images/wheel_original.png')
    return surface

def create_options_dict(options_list):
    options_dict = {}
    for count, text_angle in enumerate(range(23,383,45)):
        option_number = f'option_{count+1}'
        options_dict[option_number] = (options_list[count], text_angle)
    return options_dict

def validate_files(original_wheel):
    """
    """
    missing_files = 0
    for angle in range(0,361,1):
        wheel_path = 'assets/images/rotated_wheels/rotated_wheel_' + \
            str(angle) + '.png'
        if check_file(wheel_path) is False:
            missing_files += 1
            rotated_wheel = rotate_wheel(original_wheel, angle)
            save_file(rotated_wheel, wheel_path)
    print(f'All files validated. {str(missing_files)} files were missing!')

def create_new_wheel_files(blank_wheel, options_list, length, height):
    options_dict = create_options_dict(options_list)
    original_wheel = create_wheel(blank_wheel, length, height, options_dict)
    reference = shelve.open('reference')
    try:
        if reference['options'] != options:
            for angle in range(0,361,1):
                wheel_path = 'assets/images/rotated_wheels/rotated_wheel_' + \
                    str(angle) + '.png'
                rotated_wheel = rotate_wheel(original_wheel, angle)
                save_file(rotated_wheel, wheel_path)
    except:
        for angle in range(0,361,1):
            wheel_path = 'assets/images/rotated_wheels/rotated_wheel_' + \
                str(angle) + '.png'
            rotated_wheel = rotate_wheel(original_wheel, angle)
            save_file(rotated_wheel, wheel_path)   
    reference.close()

def generate_random_number(range=(0,361)):
    random.seed()
    random_number = random.randrange(range[0],range[1],5)
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

def find_text_location():
    text_locations = {}
    coord_pairs = {1:[(297.125,234.375),(437.5,187.5)],2:[(265.625,203.125),(312.5,62.5)],3:[(203.125,203.125),(187.5,62.5)],4:[(203.125,234.375),(62.5,187.5)],5:[(203.125,265.625),(62.5,312.5)],6:[(203.125,296.875),(187.5,437.5)],7:[(265.625,296.875),(312.5,437.5)],8:[(297.125,265.625),(437.5,312.5)]}
    for option in range(1,9):
        option_coords = find_midpoint(coord_pairs[option][0],coord_pairs[option][1])
        text_locations[option] = option_coords[0] + 75, option_coords[1] + 75
    return text_locations
    
def find_midpoint(coord1, coord2):
    return ((coord1[0]+coord2[0])/2, (coord1[1]+coord2[1])/2)


        


