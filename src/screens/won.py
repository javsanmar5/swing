import pygame
import sys

def won(screen, clock, width, height):
    options = ["Next level", "Exit to menu"]
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
                    if options[selected] == "Exit to menu":
                        return "exit_to_menu" 
                    elif options[selected] == "Next level":
                        return "next_level"
                    else:
                        print("Something went wrong")
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        current_width, current_height = screen.get_size()
        screen.fill((0, 0, 0))

        won_text = font.render("Congratulations! You passed the level.", True, "green")
        won_rect = won_text.get_rect(center=(current_width // 2, current_height // 2 + -1 * 50))
        screen.blit(won_text, won_rect)

        for i, option in enumerate(options):
            color = (255, 255, 255) if i == selected else (100, 100, 100)
            text = font.render(option, True, color)
            rect = text.get_rect(center=(current_width // 2, current_height // 2 + i * 50))
            screen.blit(text, rect)
        pygame.display.flip()
        clock.tick(60)

