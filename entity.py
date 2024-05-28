import pygame

class Entity:
    def __init__(self, surf: pygame.Surface, x: int, y: int, window: pygame.Surface, visible: boolean=False, scale: int=1) -> None:
        self.surf = surf.convert_alpha()
        self.x = x
        self.y = y
        self.window = window
        self.height = self.surf.get_height()
        self.width = self.surf.get_width()
        self.visible = visible
        self.health = -1

    def get_opp_corner(self) -> list[int]:
        return [self.x + self.width, self.y + self.height]

    def draw(self) -> None:
        if self.visible:
            if ((0 - self.width) < self.x < self.window.get_width()) and ((0 - self.height) < self.y < self.window.get_height()):
                self.window.blit(self.surf, [self.x, self.y])
            else:
                self.visible = False
