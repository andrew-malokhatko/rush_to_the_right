from layers.BaseLayer import *
from game.toolbar import ToolBar
from game.editor import Editor
from game.editable_map import Map 

class EditorLayer(BaseLayer):
    def __init__(self, surface, send_event: Callable):
        super().__init__(surface, send_event)
        self.level = None
        save_button = Button(120, 70, 1600, 200, self.save, Text(50, "Save", (100, 100, 100)))
        self.buttons.extend([save_button])

    def save(self):
        self.editor.save_map(self.path, self.map.blocks)

    def update(self):
        events  = pygame.event.get()
        super().update(events)
        self.map.draw(self.surface)
        self.toolbar.draw(self.surface)
        for event in events:
            self.toolbar.on_event(event)
            self.map.on_event(event, self.toolbar.id, self.map.cur_pos)
            self.move(event)

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT and self.map.cur_pos < 100:
                self.map.cur_pos += 10
                self.map.place_blocks()
            if event.key == K_LEFT and self.map.cur_pos > 9:
                self.map.cur_pos -= 10
                self.map.place_blocks()

    def on_enable(self):
        self.editor = Editor()
        self.path = Path(__file__).parent.parent / "my_levels" / self.level
        blocks_args = self.editor.load_map(self.path)
        self.map = Map(360, 300, 1200, 400)

        self.toolbar = ToolBar(self.surface)
        self.map.place_blocks(blocks_args)