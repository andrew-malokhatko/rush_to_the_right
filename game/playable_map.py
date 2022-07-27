import pygame
from game.block import *

class Map:
    def __init__(self, x, y, width, height):
        """give width / height as 3 / 1"""
        self.x = x
        self.y = y
        self.size = height / 10
        self.image = pygame.Surface((width, height))
        self.image.fill((40, 40, 40))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.cur_pos = 0
        self.blocks = {}
        self.finish = None

    def get_blocks(self, blocks_args):
        for bl in blocks_args:
            self.blocks[bl[0], bl[1]] = Block(bl.id, bl.x * self.size, bl.y * self.size, self.size)

            if bl.id == 2:
                self.finish = bl.x

        width = int(bl.x * self.size)
        height = int(self.size * 10)
        self.level_surface = pygame.Surface((width, height))
        return

    def fill_surface(self):
        for block in self.blocks:
            self.level_surface.blit(self.blocks[block].image, self.blocks[block].rect)

    def draw(self, surface: pygame.Surface):
        self.image.blit(self.level_surface, (self.size * self.cur_pos, 0))
        surface.blit(self.image, self.rect)

    def move(self, move):
        print(self.cur_pos + 30, "<", self.finish)
        if abs(self.cur_pos) + 30 <= self.finish:
            self.cur_pos += move
