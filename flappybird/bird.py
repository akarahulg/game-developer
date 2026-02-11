

import pygame
from settings import *


class Bird(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.bird_frames = [
            pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha(),
            pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
            pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha(),
            pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha(),
        ]

        self.bird_index = 0.0
        self.image = self.bird_frames[int(self.bird_index)]
        self.rect = self.image.get_rect(center=pos)

        self.velocity = 0.0


    def update(self):
        # animate
        self.bird_index = (self.bird_index + ANIMATION_SPEED) % len(self.bird_frames)
        self.image = self.bird_frames[int(self.bird_index)]

        self.velocity += GRAVITY
        if self.rect.y <= 450:
            self.rect.y += int(self.velocity)
            self.image = pygame.transform.rotate(self.image, -self.velocity * 3)
        else:
            self.image = pygame.transform.rotate(self.image, -90)

    def flap(self):
        self.velocity = -JUMP_SPEED






        



        
    




    
    



    


