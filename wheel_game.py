import pygame
from wheel_controller import get_mouse_position
from wheel_view import play_click_sound
from wheel_view import View
from wheel_model import Screen, divide_final_spin, generate_random_number, validate_files
import sys
from wheel_view import load_wheel_image
from wheel_model import generate_random_number
from wheel_controller import get_rig_key
from wheel_view import play_wheel_click_sound

# TO DO LIST
# -Clean up rotated images
# -Fix sounds ie add variety, etc
# - Unit tests
# - Comments

def initial():
    global game
    game = Screen()
    View(game).start_draw()
    validate_files(View(game).wheel)
    global rotated_wheel_dict
    rotated_wheel_dict = load_wheel_image()

def main():
    spin_number = 0
    target_spin_number = 3
    if game._rig is True:
        game._rig_key = get_rig_key()
    while spin_number != target_spin_number:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if View(game)._spin_button_rect.collidepoint(get_mouse_position()):
                play_click_sound(game.BUTTON_CLICK_SOUND)
                game._start_game = True
        if game._start_game is True:
            game._wheel_angle -= 5
            if game._wheel_angle <= -360:
                game._wheel_angle = game._wheel_angle + 360
                if target_spin_number - spin_number == 1:
                    if game._rig is False:
                        final_spin = divide_final_spin(generate_random_number())
                    else:
                        final_spin = divide_final_spin(generate_random_number(game.RIG_DICT[game._rig_key]))
                    for increment in final_spin:
                        game._wheel_angle -= increment
                        if game._wheel_angle <= -360:
                            game._wheel_angle = game._wheel_angle + 360
                        View(game).main_draw(rotated_wheel_dict)
                        # play_wheel_click_sound(game.WHEEL_CLICK_SOUND)
                spin_number += 1
        View(game).main_draw(rotated_wheel_dict)
        # play_wheel_click_sound(game.WHEEL_CLICK_SOUND)
    game._new_game = True
    if game._new_game == True:
        game._start_game = False
        main()




if __name__ == "__main__":
    initial()
    main()