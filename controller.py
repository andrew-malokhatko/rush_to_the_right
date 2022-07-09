import pygame
from layers import *

class Controller:
    def __init__(self, id, surface: pygame.Surface):
        self.cur_layer = id
        self.layers = {}
        self.surface = surface
        for item in globals():
            if item.endswith("Layer"):
                layer_cls = globals()[item]
                self.layers[layer_cls.id] = layer_cls(self.surface, self.set_layer)

    def set_layer(self, new_id):
        self.cur_layer = new_id

    def main_loop(self):
        timer = pygame.time.Clock()
        while True:
            self.surface.fill((0, 0, 0))
            layer = self.layers[self.cur_layer]
            layer.update()
            timer.tick(60)
            pygame.display.flip()
        