import pygame
from wheel_controller import get_mouse_position
from wheel_view import play_click_sound
from wheel_view import View
from wheel_model import Screen, validate_files
import sys
from wheel_view import load_wheel_image

def main():
    game = Screen()
    validate_files(View(game).wheel)

    spin_number = 0
    while spin_number != 3:
        View(game).main_draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if View(game)._spin_button_rect.collidepoint(get_mouse_position()):
                play_click_sound()
                game._start_game = True
        if game._start_game is True:
            game._wheel_angle -= 25
            if game._wheel_angle <= -360:
                game._wheel_angle = game._wheel_angle + 360

    game._new_game = True

    if game._new_game == True:
        main()




if __name__ == "__main__":
    main()