from settings import *
import pygame
from button import Button
from colors import Colors
from sys import exit

class Menu:
    def __init__(self, game):
        self.game = game
        self.main_surface = pygame.display.get_surface()
        self.menu_x = GAME_WIDTH + PADDING * 2
        self.menu_y = GAME_HEIGHT - PADDING - MENU_HEIGHT


        self.start_button = Button(
            self.menu_x, self.menu_y, 150, 40,
            "RESTART",
            Colors.TETRIS_COLORS['-'],
            self.game.restart
        )

        self.quit_button = Button(
            self.menu_x,self.menu_y + 40, 150, 40,
            "QUIT",
            Colors.TETRIS_COLORS['-'],
            self.quit_game
            
        )

    def draw(self):
        self.start_button.draw(self.main_surface)
        self.quit_button.draw(self.main_surface)

    def quit_game(self):
        pygame.quit()
        exit()

    def handle_event(self, event):
        self.start_button.handle_event(event)
        self.quit_button.handle_event(event)

    def update_hover(self, mouse_pos):
        self.start_button.update_hover(mouse_pos)
        self.quit_button.update_hover(mouse_pos)
