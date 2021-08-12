import pygame
from wheel_controller import get_mouse_position, get_rig_key
from wheel_view import View, play_click_sound, play_wheel_click_sound, \
    load_wheel_image
from wheel_model import Screen, divide_final_spin, generate_random_number, \
    validate_files
import sys
import time

# TO DO LIST
# - Clean up rotated images
# - Fix sounds ie add variety, etc
# - Unit tests
# - Comments
# - Restructure (image paths shuold go through the model)

def initial():
    """
    Initializes the following:
        - Screen Class
        - View Class
        - Checks and loads all wheel images
        - Add variable config file for executable
    """
    start = time.time()
    global game
    global final_spin
    global rotated_wheel_dict # Set to global so other functions can use.
    game = Screen()
    View(game).start_draw()
    validate_files(View(game).wheel)
    rotated_wheel_dict = load_wheel_image()
    end = time.time()
    print(f'Successfully initialized in {end - start}')

def main():
    """
    Initializes main loop.
    """
    spin_number = 0
    target_spin_number = 3 # Wheel will spin a minimum of 3 times.
    if game._rig is True:
        game._rig_key = get_rig_key(game.RIG_DICT)
    if game._rig is False:
        final_spin = divide_final_spin(generate_random_number())
    else:
        final_spin = divide_final_spin(generate_random_number( \
            game.RIG_DICT[game._rig_key]))
    while spin_number != target_spin_number:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if View(game)._spin_button_rect.collidepoint(get_mouse_position()):
                play_click_sound(game.BUTTON_CLICK_SOUND)
                game._start_game = True # Start game if button is clicked.
        if game._start_game is True:
            game._wheel_angle -= 5 # Wheel will move at 5 degree intervals.
            if game._wheel_angle <= -360: # Reset angle to zero degrees.
                game._wheel_angle = game._wheel_angle + 360
                if target_spin_number - spin_number == 1: # Determines how \
                    # much more to spin after 3rd spin.
                    play_wheel_click_sound(game.WHEEL_CLICK_SOUND)
                    for increment in final_spin:
                        game._wheel_angle -= increment
                        if game._wheel_angle <= -360:
                            game._wheel_angle = game._wheel_angle + 360
                        View(game).main_draw(rotated_wheel_dict)
                spin_number += 1
        View(game).main_draw(rotated_wheel_dict)
    game._start_game = False
    main()




if __name__ == "__main__":
    initial()
    main()