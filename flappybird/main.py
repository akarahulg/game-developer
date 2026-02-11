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
        self.bird = Bird()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
            self.clock.tick(FPS)

            self.game.run()

        pygame.quit()

if __name__ == "__main__":
    flappybird = FlappyBird()
    flappybird.run()


            
