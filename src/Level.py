import pygame
import os
from entities.Player import Player 

OBSTACLE_IMAGE = pygame.image.load(os.path.join('assets', 'stone_brick.png'))


class Level:
    def __init__(self, layout):
        self.layout = layout
        self.rows = len(layout)
        self.cols = len(layout[0]) if self.rows > 0 else 0
        self.players = []
        self.obstacles = []
        self.win_pos = None
        self.won = False
        self.parse_layout()

    def parse_layout(self):
        for y, row in enumerate(self.layout):
            for x, tile in enumerate(row):
                if tile == "1":
                    player = Player(x, y, "cyan2")
                    self.players.append(player)
                elif tile == "2":
                    player = Player(x, y, "coral")
                    self.players.append(player)
                elif tile == "X":
                    self.obstacles.append((x, y))
                elif tile == "W":
                    self.win_pos = (x, y)

    def draw(self, surface):
        width, height = surface.get_size()
        tile_w = width / self.cols
        tile_h = height / self.rows

        for y, row in enumerate(self.layout):
            for x, tile in enumerate(row):
                rect = pygame.Rect(x * tile_w, y * tile_h, tile_w, tile_h)
                color = (100, 100, 100) if (x + y) % 2 == 0 else (120, 120, 120)
                pygame.draw.rect(surface, color, rect)

        for player in self.players:
            x, y = player.x, player.y 
            rect = pygame.Rect(x * tile_w, y * tile_h, tile_w, tile_h)
            pygame.draw.rect(surface, player.color ,rect)
        
        for (x, y) in self.obstacles:
            rect = pygame.Rect(x * tile_w, y * tile_h, tile_w, tile_h)
            obstacle_resized = pygame.transform.scale(OBSTACLE_IMAGE, (tile_w, tile_h))
            surface.blit(obstacle_resized, rect)

        if self.win_pos: 
            win_rect = pygame.Rect(self.win_pos[0] * tile_w, self.win_pos[1] * tile_h, tile_w, tile_h)
            pygame.draw.rect(surface, "bisque", win_rect) 

    def update(self, screen, dt) -> None:
        keys = pygame.key.get_pressed()
        for player in self.players:
            player.update(keys, self.cols, self.rows, self.obstacles)
        self._check_won()
        self.draw(screen)
        
    def _check_won(self) -> None:
        if self.win_pos:
            for player in self.players:
                if not player.has_won(self.win_pos):
                    self.won = False
                    return
            self.won = True

