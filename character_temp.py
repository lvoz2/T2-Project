from dynentity import DynEntity
from screen import Screen
import pygame
import math

class Character(DynEntity):
    def __init__(self, surf: pygame.Surface, x: int, y: int, window: pygame.Surface, name: str, character_class: str, defense: int=10, mana: int=10, strength: int=10, scale: int=1) -> None:
        super().__init__(surf, x, y, window, 100, True, scale)
        self.name = name
        self.character_class = character_class
        self.defense: int = defense
        self.mana: int = mana
        self.strength: int = strength
        self.lvl: int = 0
        self.xp: int = 0
        self.skills: dict[str, Any] = {}
        self.inventory: list[Any] = []
        self.money: int = 0
        self.attr_pts: int = 0
        self.ATTR_PTS_PER_LVL: int = 3
        self.MAX_LVL: int = 50

    def assign_attr_pts(self, attr: str, pts: int) -> None:
        if attr in self.__dict__:
            setattr(self, attr, getattr(self, attr) + pts)
            self.attr_pts -= pts
        else:
            raise KeyError("Character attribute does not exist")

    def gain_xp(self, xp: int, screen: Screen) -> None:
        self.xp += xp
        req_xp: int = self.calc_req_xp(self.lvl + 1)
        while self.xp >= req_xp and self.lvl < self.MAX_LVL:
            self.lvl += 1
            self.xp -= req_xp
            self.attr_pts += self.ATTR_PTS_PER_LVL
            # screen.show("Level Up", f"{self.name} is now level {self.level}")
            req_xp: int = self.calc_req_xp(self.lvl + 1)

    def calc_req_xp(self, lvl: int) -> int:
        return int(100 * floor(1.5 ** (lvl - 1)))