import pygame
from wheel_controller import get_mouse_position
from wheel_view import play_click_sound
from wheel_view import View
from wheel_model import Screen
import sys

def main():
    game = Screen()

    # clock = pygame.time.Clock()

    while game._wheel_angle != -1080:
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
            game._wheel_angle -= 1

    game._new_game = True

    if game._new_game == True:
        main()




if __name__ == "__main__":
    main()