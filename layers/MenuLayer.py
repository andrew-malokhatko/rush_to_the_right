from layers.BaseLayer import *

class MenuLayer(BaseLayer):
    def __init__(self, surface: pygame.Surface, send_event: Callable): # remove absolute numbers (set size relatively to scr_size)
        super().__init__(surface, send_event)

        creator_button = Button(850, 100, self.surface.get_width() / 2 + 600, self.surface.get_height() / 2, lambda x = Event("change_layer", "creator"): self.events.append(x), Text(70, "Creator", (40, 40, 40), (255, 255, 255)))
        multiplayer_button = Button(850, 100, self.surface.get_width() / 2 + 600, self.surface.get_height() / 2 + 120, lambda: None, Text(70, "Multiplayer", (40, 40, 40), (255, 255, 255)))

        self.buttons.extend([creator_button, multiplayer_button])