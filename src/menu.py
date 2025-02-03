import sys
import pygame
from pygame.locals import *
from levels import load_level

def menu(screen, width, height):
    font = pygame.font.Font(None, 50)
    options = ["Level 1", "Exit"]
    selected = 0

    while True:
        screen.fill((0, 0, 0))

        for i, option in enumerate(options):
            color = (255, 255, 255) if i == selected else (100, 100, 100)
            text = font.render(option, True, color)
            rect = text.get_rect(center=(width // 2, height // 2 + i * 60))
            screen.blit(text, rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if options[selected] == "Exit":
                        pygame.quit()
                        sys.exit()
                    else:
                        level = load_level("level1")
                        level.run(screen, width, height)

