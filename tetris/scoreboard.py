from game import Game
import pygame 
from settings import *
from colors import Colors

class Score:
    def __init__(self, game):
        self.game = game
        self.score_surface = pygame.Surface((SIDE_WIDTH, SCORE_HEIGHT))
        self.main_surface = pygame.display.get_surface()
        
    def run(self):
        self.score_surface.fill(Colors.TETRIS_COLORS["-"])
        font = pygame.font.SysFont('Arial', 30)
        score_text = font.render(f'Score\n  {self.game.score}', True, (255, 255, 255))
        self.score_surface.blit(score_text, (self.score_surface.get_width() // 2 - score_text.get_width() // 2 - 10,
                                              self.score_surface.get_height() // 2 - score_text.get_height() // 2))   
        self.main_surface.blit(self.score_surface, (GAME_WIDTH + PADDING*2, GAME_HEIGHT - (SCORE_HEIGHT + PADDING) - (SIDE_BAR_FRACTION * GAME_HEIGHT)))