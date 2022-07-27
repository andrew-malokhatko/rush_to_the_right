from layers.BaseLayer import *

class LevelLayer(BaseLayer):
    def __init__(self, surface, send_event: Callable):
        super().__init__(surface, send_event)
        self.level = None
        return_button = Button(250, 100, 200, surface.get_height() / 2 - 300, lambda x = "creator" :self.to_level(x), Text(70, "Back", (40, 40, 40), (255, 255, 255)))
        self.name_entry = Entry(900, 110, surface.get_width() / 2, surface.get_height() / 2 - 300, 16, (30, 30, 30), (50, 50, 50), (255, 255, 255), 50, self.level)
        play_button = Button(250, 100, surface.get_width() / 2, surface.get_height() / 2 + 200, lambda x = "singleplayer" :self.to_level(x), Text(70, "Play", (40, 40, 40), (255, 255, 255)))
        edit_button = Button(250, 100, surface.get_width() / 2 - 300, surface.get_height() / 2 + 200, lambda x = "editor" :self.to_level(x), Text(70, "Edit", (40, 40, 40), (255, 255, 255)))
        self.entries.extend([self.name_entry])
        self.buttons.extend([return_button, play_button, edit_button])

    def to_level(self, layer):
        self.events.append(Event("change_layer", layer))
        self.events.append(Event("set_level", self.level))

    def on_enable(self):
        self.name_entry.text = self.level