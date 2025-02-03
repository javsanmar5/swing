# main.py
import pygame
import sys
from Level import Level
from menu import menu

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

levels = {
    "Level 1": [
        "0000000000000000000000000",
        "0000000000000000000000000",
        "001000X000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000200000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",
        "0000000000000000000000000",

    ],
}

def main():
    global screen, WIDTH, HEIGHT
    options = list(levels.keys())
    options.append("EXIT")
    current_level_name = menu(screen, clock, WIDTH, HEIGHT, options)
    level_layout = levels[current_level_name]
    level_instance = Level(level_layout)
    while True:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        screen.fill((0, 0, 0))
        level_instance.update(screen, dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()

