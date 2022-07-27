from collections import namedtuple
import pygame
from classes import *
from typing import Callable

Event = namedtuple("Event", ["type", "data"])

class BaseLayer:

    def __init__(self, surface: pygame.Surface, send_event: Callable): # pass func to
        self.surface = surface
        self.send_event = send_event
        self.buttons = []
        self.entries = []
        self.events = []

    def update(self, events = None):

        if events == None:
            events = pygame.event.get()

        self.load_events()

        for button in self.buttons:
            button.draw(self.surface)
            for event in events:
                button.on_event(event)

        for entry in self.entries:
            entry.draw(self.surface)
            entry.update()
            for event in events:
                entry.on_event(event)

    def load_events(self):
        for event in self.events:
            self.send_event(event)

    def on_enable(self):
        pass