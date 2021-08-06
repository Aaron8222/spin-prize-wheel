import pygame
from wheel_controller import get_mouse_position
from wheel_view import play_click_sound
from wheel_view import View
from wheel_model import Screen, validate_files
import sys
from wheel_view import load_wheel_image


def initial():
    global game
    game = Screen()
    validate_files(View(game).wheel)
    global rotated_wheel_dict
    rotated_wheel_dict = load_wheel_image()
    

def main():
    spin_number = 0
    while spin_number != 3:
        View(game).main_draw(rotated_wheel_dict)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if View(game)._spin_button_rect.collidepoint(get_mouse_position()):
                play_click_sound()
                game._start_game = True
        if game._start_game is True:
            game._wheel_angle -= 5
            if game._wheel_angle <= -360:
                game._wheel_angle = game._wheel_angle + 360
                spin_number += 1

    game._new_game = True

    if game._new_game == True:
        game._start_game = False
        main()




if __name__ == "__main__":
    initial()
    main()