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
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXXX00000XXXXXXXXXX",
        "XXXXXXXXXX0XXX0XXXXXXXXXX",
        "XXXXXXXXXX0XXX0XXXXXXXXXX",
        "XXXXXXXXXX0XXX0XXXXXXXXXX",
        "XXXXXXXXXX0XXX0XXXXXXXXXX",
        "XXXXXXXXXX0XXX0XXXXXXXXXX",
        "XXXXXXXXXX0XXX0XXXXXXXXXX",
        "XXXXXXXXXX0XXX0XXXXXXXXXX",
        "XXXXXXXXXX0XXX0XXXXXXXXXX",
        "XX000000000XXX000000000XX",
        "XX0XXXXXXXXXXXXXXXXXXX0XX",
        "XX0XXXXXXXXXXXXXXXXXXX0XX",
        "XX0XXXXXXXXXXXXXXXXXXX0XX",
        "XX0XXXXXXXXXXXXXXXXXXX0XX",
        "XX0XXXX1XXXXXXXXX2XXXX0XX",
        "XX0XXXX0XXXXXXXXX0XXXX0XX",
        "XX0XXXX0XXXXXXXXX0XXXX0XX",
        "XX000000XXXXXXXXX000000XX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",

    ],
    "Level 2": [
        "XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XXXXXXXXX000000XXXXXXXXXX",
        "XXXXXXXXX0XXXX0XXXXXXXXXX",
        "XXXXXXXXX0XXXX0XXXXXXXXXX",
        "XXXXXXXXX0XXXX0XXXXXXXXXX",
        "XXXXXXXXX0XXXX0XXXXXXXXXX",
        "XXXXXXXXX0XXXX0XXXXXXXXXX",
        "XXXXX000000000000000XXXXX",
        "XXXXX0XXX0XXXX0XXX00XXXXX",
        "XX0XX0XXX0XXXX0XXX00XXXXX",
        "XX000000000000000000XXXXX",
        "XX0XX0XXX0XXXX0XXX0XXXXXX",
        "XX0XX0XXX0XXXX0XXX00XXXXX",
        "XX0XX0XXX0XXXX0XXX00XXXXX",
        "XX0XX0XXX0XXXX0XXXXXXXXXX",
        "XX00000000XXXX0XXXXXXXXXX",
        "XXXXX0XXXXX0XX0XXXXXXXXXX",
        "XXXXX0XXXXX0002XXXXXXXXXX",
        "XXXXX1XXXXX0XXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",

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

