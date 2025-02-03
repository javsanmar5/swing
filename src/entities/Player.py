import pygame

class Player:
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.color = color

    def update(self, keys, cols, rows, obstacles):
        dx, dy = 0, 0

        if keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_RIGHT]:
            dx += 1
        if keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_DOWN]:
            dy += 1

        new_x = self.x + dx
        new_y = self.y + dy

        if (new_x, new_y) in obstacles:
            return

        new_x = max(0, min(new_x, cols - 1))
        new_y = max(0, min(new_y, rows - 1))

        self.x = new_x
        self.y = new_y
