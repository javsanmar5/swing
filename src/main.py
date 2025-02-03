import sys
import pygame
from pygame.locals import *
from menu import menu

TILE_SIZE = 32  

def run_game() -> None:
    pygame.init()

    fps = 60.0
    fpsClock = pygame.time.Clock()

    info = pygame.display.Info()
    width, height = info.current_w, info.current_h
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    menu(screen, width, height)

def game_loop(screen, width, height):
    fps = 60.0
    fpsClock = pygame.time.Clock()
    last_time = pygame.time.get_ticks()

    while True:
        now = pygame.time.get_ticks()
        dt = (now - last_time) / 1000.0
        last_time = now

        update()
        draw(screen, width, height)

        fpsClock.tick(fps)

def draw(screen, width, height) -> None:
    screen.fill((0, 0, 0))

    for x in range(0, width, TILE_SIZE):
        for y in range(0, height, TILE_SIZE):
            pygame.draw.rect(screen, (50, 50, 50), (x, y, TILE_SIZE, TILE_SIZE), 1)

    pygame.display.flip()

def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    run_game()

