import sys
 
import pygame
from pygame.locals import *


def run_game() -> None:
    pygame.init()

    fps = 60.0
    fpsClock = pygame.time.Clock()

    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    dt = 1/fps 
    while True: 
        update(dt) 
        draw(screen)

        dt = fpsClock.tick(fps)

def draw(screen) -> None:
    screen.fill((0, 0, 0)) 
    pygame.display.flip()

def update(dt):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 

if __name__=="__main__":
    run_game()
