from layers.BaseLayer import *
from game.editor import Editor
from game.hero import Hero
from game.playable_map import Map

class SinglePlayerLayer(BaseLayer):
    def __init__(self, surface, send_event: Callable):
        super().__init__(surface, send_event)
        self.level = None

    def update(self):
        events = pygame.event.get()
        self.move(events)
        self.map.draw(self.surface)
        self.hero.draw(self.surface, self.map.cur_pos)

        super().update(events)

    def move(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:

                if event.key == K_RIGHT and self.valid_move(self.hero.x + 1, self.hero.y):
                    i = 1
                    while (self.valid_move(self.hero.x + i + 1, self.hero.y)):
                        i+=1
                    self.hero.x += i
                    self.map.move(-i)

                if event.key == K_LEFT and self.valid_move(self.hero.x - 1, self.hero.y):
                    i = 1
                    while (self.valid_move(self.hero.x - i - 1, self.hero.y)):
                        i+=1
                    self.hero.x -= i
                    self.map.move(i)

                if event.key == K_DOWN and self.valid_move(self.hero.x, self.hero.y + 1):
                    i = 1
                    while (self.valid_move(self.hero.x, self.hero.y + i + 1)):
                        i+=1
                    self.hero.move(i)

                if event.key == K_UP and self.valid_move(self.hero.x, self.hero.y - 1):
                    i = 1
                    while (self.valid_move(self.hero.x, self.hero.y - i - 1)):
                        i+=1
                    self.hero.move(-i)

    def valid_move(self, hero_x, hero_y):
        if hero_x < 0 or hero_y < 0:
            return False
        if hero_y > 9:
            return False
        if self.map.blocks[hero_x, hero_y].id == 1:
            return False
        return True

    def on_enable(self):
        self.editor = Editor()
        self.path = Path(__file__).parent.parent / "my_levels" / self.level
        blocks_args = self.editor.load_map(self.path)

        self.map = Map(360, 300, 1200, 400)
        self.map.get_blocks(blocks_args)
        self.map.fill_surface()

        self.hero = Hero(5, 5, self.map.size, self.map.x, self.map.y)