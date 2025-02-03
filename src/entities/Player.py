import pygame

class Player:
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.locked_direction = None

    def update(self, keys, cols, rows, obstacles):
        if self.locked_direction is None:
            if keys[pygame.K_LEFT]:
                self.locked_direction = (-1, 0)
            elif keys[pygame.K_RIGHT]:
                self.locked_direction = (1, 0)
            elif keys[pygame.K_UP]:
                self.locked_direction = (0, -1)
            elif keys[pygame.K_DOWN]:
                self.locked_direction = (0, 1)

        if self.locked_direction is not None:
            dx, dy = self.locked_direction
            new_x = self.x + dx
            new_y = self.y + dy

            if (new_x, new_y) in obstacles:
                self.locked_direction = None
                return

            if new_x < 0 or new_x >= cols or new_y < 0 or new_y >= rows:
                self.locked_direction = None
                return

            self.x = new_x
            self.y = new_y

