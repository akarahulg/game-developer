

import pygame
from settings import *

class Bird(pygame.sprite.Sprite):
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.bird = pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha()
        self.bird_rect = self.bird.get_rect()
        self.bird_rect.center = (100, GAME_HEIGHT //2)
        self.display_surface.blit(self.bird, self.bird_rect)


        



        
    




    
    



    


