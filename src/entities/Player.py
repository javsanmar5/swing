import pygame

class Player:
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.locked_direction = None
        self.open_keys = 0
        self.to_open_door = False
    
    def update(self, keys, cols, rows, obstacles, doors, open_keys):
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

            if (new_x, new_y) in open_keys:
                open_keys.remove((new_x, new_y))
                self.open_keys += 1

            if (new_x, new_y) in obstacles or (new_x, new_y) in doors:
                self.locked_direction = None
                if (new_x, new_y) in doors and self.open_keys >= 1:
                    if self.to_open_door:
                        doors.remove((new_x, new_y))
                        self.open_keys -= 1
                        self.open_door = False
                    else:
                        self.to_open_door = True
                return

            if new_x < 0 or new_x >= cols or new_y < 0 or new_y >= rows:
                self.locked_direction = None
                return

            self.x = new_x
            self.y = new_y

    def has_won(self, win_pos: tuple) -> bool:
        return self.x == win_pos[0] and self.y == win_pos[1] 


