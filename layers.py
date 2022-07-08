import pygame
import pygame.freetype
from classes import *

__all__ = ["MenuLayer"]

class BaseLayer:
    def __init_subclass__(self, id: int):
        self.id = id
    
    def __init__(self, surface):
        self.surface = surface
        self.objects = []

    def update(self):
        for object in self.objects:
            object.draw(self.surface)

        
class MenuLayer(BaseLayer, id = 0):
    def __init__(self, surface: pygame.Surface):
        super().__init__(surface)
        solo_button = Button(850, 100, self.surface.get_width() / 2 + 400, self.surface.get_height() / 2, lambda:None, Text(70, "Solo", (40, 40, 40), (255, 255, 255)))
        multiplayer_button = Button(850, 100, self.surface.get_width() / 2 + 400, self.surface.get_height() / 2 + 120, lambda:None, Text(70, "Multiplayer", (40, 40, 40), (255, 255, 255)))
        self.objects.extend([solo_button, multiplayer_button])