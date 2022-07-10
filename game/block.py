import pygame

class Block():
    def __init__(self, id, x, y):
        self.size = 30   # block size to change
        self.id = id
        self.colors = {
            0: (255, 255, 255),
            1: (100, 100, 100)
        }
        self.color = self.colors[id]
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.colors[id])
        self.rect = self.image.get_rect(center = (self.size * x + 200, self.size * y + 200))

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)