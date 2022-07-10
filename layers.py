from asyncio import selector_events
from tkinter import SEL_FIRST
import pygame
from classes import *
from typing import Callable
from game.creator import *

__all__ = ["MenuLayer", "CreatorLayer", "LevelLayer", "EditorLayer"]

class BaseLayer:
    def __init_subclass__(self, id: int):
        self.id = id
    
    def __init__(self, surface: pygame.Surface, set_layer: Callable):
        self.set_layer = set_layer
        self.surface = surface
        self.buttons = []
        self.entries = []
        self.blocks = {}

    def update(self):
        events = pygame.event.get()

        for button in self.buttons:
            button.draw(self.surface)
            for event in events:
                button.on_event(event)

        for entry in self.entries:
            entry.draw(self.surface)
            entry.update()
            for event in events:
                entry.on_event(event)

        for key in self.blocks:
            self.blocks[key].draw(self.surface)

        #self.on_enable()

    #def on_enable():
        #pass

        


class MenuLayer(BaseLayer, id = 0):
    def __init__(self, surface: pygame.Surface, set_layer: Callable):
        super().__init__(surface, set_layer)
        creator_button = Button(850, 100, self.surface.get_width() / 2 + 600, self.surface.get_height() / 2, lambda x = 1: self.set_layer(x), Text(70, "Creator", (40, 40, 40), (255, 255, 255)))
        multiplayer_button = Button(850, 100, self.surface.get_width() / 2 + 600, self.surface.get_height() / 2 + 120, lambda:None, Text(70, "Multiplayer", (40, 40, 40), (255, 255, 255)))
        self.buttons.extend([creator_button, multiplayer_button])

    def on_event(self):
        return

class CreatorLayer(BaseLayer, id = 1):
    def __init__(self, surface, set_layer: Callable):
        super().__init__(surface, set_layer)
        return_button = Button(250, 100, 200, surface.get_height() / 2 - 300, lambda x = 1: self.set_layer(x), Text(70, "Back", (40, 40, 40), (255, 255, 255)))
        new_button = Button(300, 100, self.surface.get_width() - 150, self.surface.get_height() - 200, lambda x = 2: self.set_layer(x), Text(70, "New", (40, 40, 40), (255, 255, 255)))
        i = 0
        for f in (Path(__file__).parent / "my_levels").iterdir():
            level_button = Button(700, 100, surface.get_width() / 2, 300 + 120 * i, lambda x = f.name: self.level_onclick(x), Text(70, f.name, (40, 40, 40), (255, 255, 255)))
            self.buttons.append(level_button)
            i += 1
        self.buttons.extend([new_button, return_button])

    def level_onclick(self, level_name):
        global selected_level
        selected_level = level_name
        self.set_layer(2)


class LevelLayer(BaseLayer, id = 2):
    def __init__(self, surface, set_layer: Callable):
        global selected_level
        super().__init__(surface, set_layer)
        return_button = Button(250, 100, 200, surface.get_height() / 2 - 300, lambda x = 1: self.set_layer(x), Text(70, "Back", (40, 40, 40), (255, 255, 255)))
        self.name_entry = Entry(900, 110, surface.get_width() / 2, surface.get_height() / 2 - 300, 16, (30, 30, 30), (50, 50, 50), (255, 255, 255), 50, "")
        play_button = Button(250, 100, surface.get_width() / 2, surface.get_height() / 2 + 200, lambda: None, Text(70, "Play", (40, 40, 40), (255, 255, 255)))
        edit_button = Button(250, 100, surface.get_width() / 2 - 300, surface.get_height() / 2 + 200, self.on_edit, Text(70, "Edit", (40, 40, 40), (255, 255, 255)))
        self.entries.extend([self.name_entry])
        self.buttons.extend([return_button, play_button, edit_button])

    def update(self):
        global selected_level
        super().update()
        self.name_entry.text = selected_level

    def on_edit(self):
        global selected_level
        selected_level = self.name_entry.get()
        self.set_layer(3)

class EditorLayer(BaseLayer, id = 3):
    def __init__(self, surface, set_layer: Callable):
        super().__init__(surface, set_layer)
        self.surface = surface
        
    def update(self):
        global selected_level
        super().update()
        creator = Creator(selected_level)
        blocks = creator.load_map(Path(__file__).parent / "my_levels" / selected_level) # make on_enable !!!
        self.blocks = blocks