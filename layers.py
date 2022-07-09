import pygame
from classes import *
from typing import Callable

__all__ = ["MenuLayer", "CreatorLayer"]

class BaseLayer:
    def __init_subclass__(self, id: int):
        self.id = id
    
    def __init__(self, surface, set_layer: Callable):
        self.set_layer = set_layer
        self.surface = surface
        self.objects = []

    def update(self):
        for object in self.objects:
            object.draw(self.surface)
            for event in pygame.event.get():
                object.on_event(event)


class MenuLayer(BaseLayer, id = 0):
    def __init__(self, surface: pygame.Surface, set_layer: Callable):
        super().__init__(surface, set_layer)
        creator_button = Button(850, 100, self.surface.get_width() / 2 + 400, self.surface.get_height() / 2, lambda x = 1: self.set_layer(x), Text(70, "Creator", (40, 40, 40), (255, 255, 255)))
        multiplayer_button = Button(850, 100, self.surface.get_width() / 2 + 400, self.surface.get_height() / 2 + 120, lambda:None, Text(70, "Multiplayer", (40, 40, 40), (255, 255, 255)))
        self.objects.extend([creator_button, multiplayer_button])

class CreatorLayer(BaseLayer, id = 1):
    def __init__(self, surface, set_layer: Callable):
        super().__init__(surface, set_layer)
        new_button = Button(100, 100, self.surface.get_width() - 200, self.surface.get_height() - 200, lambda:None, Text(70, "New", (40, 40, 40), (255, 255, 255)))
        self.objects.extend([new_button])