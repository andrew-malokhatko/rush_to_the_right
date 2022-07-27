import pygame
from collections import namedtuple
from game.blocks import blocks

tBlock = namedtuple("Block", "x y id")

class Block():
    def __init__(self, id, x, y, size):
        self.size = size   # block size to change
        self.id = id
        self.x = x
        self.color = blocks[id]
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft = (x, y))

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)

    def set_color(self):
        self.color = blocks[self.id]
        self.image.fill(self.color)