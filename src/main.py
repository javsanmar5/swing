# main.py
import pygame
import sys
from Level import Level
from screens.menu import menu
from screens.won import won
from levels.load_levels import load_levels

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

levels = load_levels()

def main():
    global screen, WIDTH, HEIGHT
    menu_options = list(levels.keys())
    menu_options.append("EXIT")
    current_level_name = menu(screen, clock, WIDTH, HEIGHT, menu_options)
    level_layout = levels[current_level_name]
    level_instance = Level(level_layout)
    game_state = "playing"
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

        match game_state:
            case "playing":
                level_instance.update(screen, dt)
                if level_instance.won:
                    game_state = "won"
            case "won":
                result = won(screen, clock, WIDTH, HEIGHT)
                if result == "exit_to_menu":
                    game_state = "menu"
                elif result == "next_level":
                    current_level_name = _get_next_level_name(current_level_name)
                    level_layout = levels[current_level_name]
                    level_instance = Level(level_layout)
                    game_state = "playing"
            case "menu":
                current_level_name = menu(screen, clock, WIDTH, HEIGHT, menu_options)
                level_layout = levels[current_level_name]
                level_instance = Level(level_layout)
                game_state = "playing"

        pygame.display.flip()

def _get_next_level_name(current_level_name: str) -> str:
    visited = False
    for k in levels.keys():
        if visited:
            return k
        if k == current_level_name:
            visited = True
    # TODO: Handle error when there are no more levels
    return "AAAAAAAAAAAARGHHHH"

if __name__ == "__main__":
    main()

