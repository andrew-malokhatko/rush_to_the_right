import pygame
from collections import namedtuple
from layers.LayerController import LayerController

Position = namedtuple("Position", "x y")
SCREENSIZE = Position(1920, 1080)

screen = pygame.display.set_mode(SCREENSIZE)
layer_controller = LayerController(screen)
layer_controller.main_loop()