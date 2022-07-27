from layers.BaseLayer import *

class CreatorLayer(BaseLayer):
    def __init__(self, surface, send_event: Callable):
        super().__init__(surface, send_event)
        return_button = Button(250, 100, 200, surface.get_height() / 2 - 300, lambda: None, Text(70, "Back", (40, 40, 40), (255, 255, 255)))
        new_button = Button(300, 100, self.surface.get_width() - 150, self.surface.get_height() - 200, lambda: None, Text(70, "New", (40, 40, 40), (255, 255, 255)))

        for i, f in enumerate((Path(__file__).parent.parent / "my_levels").iterdir()):
            level_button = Button(700, 100, surface.get_width() / 2, 300 + 120 * i, lambda x = f.name: self.to_level(x), Text(70, f.name, (40, 40, 40), (255, 255, 255)))
            self.buttons.append(level_button)

        self.buttons.extend([new_button, return_button])
    
    def to_level(self, name):
        self.events.append(Event("change_layer", "level"))
        self.events.append(Event("set_level", name))