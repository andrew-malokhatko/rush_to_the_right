import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, size, x_off, y_off):
        self.x = x
        self.y = y
        self.size = size
        self.x_off = x_off
        self.y_off = y_off
        self.image = pygame.Surface((self.size, self.size))

    def draw(self, surface: pygame.Surface, map_pos):
        """surface(map.self.image)"""
        actual_y = self.y * self.size + self.y_off
        actual_x = (self.x + map_pos) * self.size + self.x_off
        surface.blit(self.image, (actual_x, actual_y))

    def move(self, move):
        self.y += move