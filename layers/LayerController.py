from layers.BaseLayer import *
from layers.EditorLayer import EditorLayer
from layers.LevelLayer import LevelLayer
from layers.CreatorLayer import CreatorLayer
from layers.MenuLayer import MenuLayer
from layers.SinglePlayerLayer import SinglePlayerLayer

class LayerController:
    def __init__(self, surface: pygame.Surface):
        self.layer = MenuLayer(surface, self.load_event)
        self.surface = surface
        self.layers = { 
            "base": BaseLayer,
            "menu": MenuLayer,
            "creator": CreatorLayer,
            "level": LevelLayer,
            "editor": EditorLayer,
            "singleplayer": SinglePlayerLayer
        }

    def load_event(self, event: Event):
        if event.type == "change_layer":
            self.layer = self.layers[event.data](self.surface, self.load_event)

        if event.type == "set_level":
            self.layer.level = event.data

    def main_loop(self):

        timer = pygame.time.Clock()
        previous = None

        while True:

            if self.layer != previous or previous is None:
                self.layer.on_enable()
                previous = self.layer

            self.surface.fill((0, 0, 0))
            self.layer.update()
            timer.tick(60)
            pygame.display.flip()

        