
import pygame
from settings import *
from bird import Bird

class Game():
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.bkg = pygame.image.load('assets/sprites/background-day.png').convert_alpha()
        self.bkg = pygame.transform.scale(self.bkg, (GAME_WIDTH, GAME_HEIGHT))

        self.base = pygame.image.load('assets/sprites/base.png').convert_alpha()
        _ , self.base_height =  self.base.get_size()
        self.base = pygame.transform.scale(self.base, (GAME_WIDTH + 32, self.base_height))

        self.bkg_rect = self.bkg.get_rect()
        self.bkg_rect.topleft = [0,0]

        self.base_rect = self.base.get_rect()
        self.base_rect.bottomright = [GAME_WIDTH + 32, GAME_HEIGHT]


    def run(self):
        self.base_rect.x -= SCROLL_SPEED
        if self.base_rect.x <= -30:
            self.base_rect.bottomright = [GAME_WIDTH + 32, GAME_HEIGHT]

        self.display_surface.blit(self.bkg, self.bkg_rect)
        self.display_surface.blit(self.base, self.base_rect)
        
    




    
    



    


