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

    def place_blocks(self, blocks_args = None):
        if blocks_args != None:
            self.blocks_args = blocks_args
            for bl in self.blocks_args:
                self.blocks[bl[0], bl[1]] = Block(bl.id, bl.x * self.size, bl.y * self.size, self.size)
            return

        for i in range(self.cur_pos, (self.cur_pos + 30)):
            for k in range(10):
                if (i, k) in self.blocks:
                    block = self.blocks[i, k]
                    self.blocks[i, k] = Block(block.id, (i - self.cur_pos) * self.size, k * self.size, self.size)
                else:
                    self.blocks[i, k] = Block(0, (i - self.cur_pos) * self.size, k * self.size, self.size)

    def draw(self, surface:pygame.Surface):
        for i in range(self.cur_pos, (self.cur_pos + 30)):
            for k in range(10):
                self.blocks[i, k].draw(self.image)
        surface.blit(self.image, self.rect)

    def on_event(self, event, cur_id, cur_pos):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                x_key = int((pos[0] - self.x) / self.size + cur_pos)
                y_key = int((pos[1] - self.y) / self.size)

                self.blocks[x_key, y_key].id = cur_id
                self.blocks[x_key, y_key].set_color()