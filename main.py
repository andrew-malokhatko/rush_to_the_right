import pygame
from collections import namedtuple
from controller import *
from layers import *

Position = namedtuple("Position", "x y")
SCREENSIZE = Position(1920, 1080)

screen = pygame.display.set_mode(SCREENSIZE)
controller = Controller(MenuLayer.id, screen)

game_on = True

controller.main_loop()
