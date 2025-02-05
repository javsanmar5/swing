# menu.py
import pygame
import sys

def menu(screen, clock, width, height, options):
    font = pygame.font.SysFont(None, 40)
    selected = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if options[selected] == "EXIT":
                        pygame.quit()
                        sys.exit()
                    return options[selected]
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        current_width, current_height = screen.get_size()
        screen.fill((0, 0, 0))
        for i, option in enumerate(options):
            color = (255, 255, 255) if i == selected else (100, 100, 100)
            text = font.render(option, True, color)
            rect = text.get_rect(center=(current_width // 2, current_height // 2 + i * 50))
            screen.blit(text, rect)
        pygame.display.flip()
        clock.tick(60)

