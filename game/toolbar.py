import pygame
from game.blocks import blocks

class Tool(pygame.sprite.Sprite):
    def __init__(self, x, y, color, id, change_id):
        self.x =x
        self.y = y
        self.color = color
        self.id = id
        self.change_id = change_id
        self.bg = pygame.Surface((70, 70)) # tool_size
        self.fg = pygame.Surface((50, 50))
        self.fg.fill(self.color)
        self.bg_rect = self.bg.get_rect(topleft = (x, y))
        self.fg_rect = self.fg.get_rect(topleft = (x + 10, y + 10)) 
    
    def draw(self, surface: pygame.Surface):
        surface.blit(self.bg, self.bg_rect)
        surface.blit(self.fg, self.fg_rect)

    def on_event(self, point):
        print(self.bg_rect, point)
        if self.bg_rect.collidepoint(point):
            self.change_id(self.id)

class ToolBar():
    def __init__(self, surface: pygame.Surface):
        self.x = surface.get_width() / 2 - 500
        self.y = surface.get_height() - 300
        self.width = 1000
        self.height = 300
        self.id = 0
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 30, 30))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.tools = []

        for i in range(len(blocks)):
            tool = Tool(100 * i + 20, 30, blocks[i], i, self.change_id)
            self.tools.append(tool)

    def change_id(self, new_id):
        self.id = new_id
        print(self.id)

    def draw(self, surface: pygame.Surface):
        for t in self.tools:
            t.draw(self.image)
        surface.blit(self.image, self.rect)

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            point = pygame.mouse.get_pos()
            if self.rect.collidepoint(point):
                for t in self.tools:
                    t.on_event((point[0] - self.x, point[1]-self.y))