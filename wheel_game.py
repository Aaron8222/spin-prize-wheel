import pygame
from wheel_controller import get_mouse_position
from wheel_view import play_click_sound
from wheel_view import View
from wheel_model import Screen

def main():
    game = Screen()

    clock = pygame.time.Clock()

    while True:
        View(game).main_draw()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if View.spin_button_rect.collidepoint(get_mouse_position()):
            play_click_sound()
            self._board.start_game = True
            game._wheel_angle += 1



if __name__ == "__main__":
    main()