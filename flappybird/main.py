#!/usr/bin/env python3
import pygame
from settings import *
from game import Game
from bird import Bird

class FlappyBird:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((GAME_WIDTH , GAME_HEIGHT))
        pygame.display.set_caption('FlappyBird')

        self.clock = pygame.time.Clock()
        self.GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.GAME_UPDATE, TICK)
        
        self.game = Game()
        self.bird = Bird((100, GAME_HEIGHT //2))
        self.bird_group = pygame.sprite.Group(self.bird)

        self.fly = True
        self.running = True

    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.fly is True:
                        self.bird.flap()

            self.game.run()

            if self.bird.rect.y >= 450:
                self.fly = False
            if self.fly:
                self.bird_group.update() 
            self.bird_group.draw(self.display_surface)


            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    flappybird = FlappyBird()
    flappybird.run()



