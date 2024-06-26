from character import Character
#from screen import Screen
import pygame
import math

class Player(Character):
    def __init__(self, surf: pygame.Surface, x: int, y: int, window: pygame.Surface, name: str, character_class: str, scale: int=1, defense: int=10, mana: int=10, strength: int=10, stamina: int=10, stamina_regen_speed: int=1) -> None:
        super().__init__(surf, x, y, window, name, health_regen_speed, 100, True, scale, defense, mana, strength)
        self.character_class = character_class
        self.stamina: int = stamina
        self.stamina_regen_speed = stamina_regen_speed
        self.max_stamina: int = 
        self.xp: int = 0
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

    def gain_xp(self, xp: int) -> None:
        self.xp += xp
        req_xp: int = self.calc_req_xp(self.lvl + 1)
        while self.xp >= req_xp and self.lvl < self.MAX_LVL:
            self.lvl += 1
            self.xp -= req_xp
            self.attr_pts += self.ATTR_PTS_PER_LVL
            # screen.show("Level Up", f"{self.name} is now level {self.level}")
            req_xp: int = self.calc_req_xp(self.lvl + 1)

    def calc_req_xp(self, lvl: int) -> int:
        return int((100 / 2) * lvl * (1 + lvl))
    
    def regen_stamina(self) -> None:
        if (self.stamina + self.stamina_regen_speed) <= self.max_stamina:
            self.stamina += self.stamina_regen_speed
        else:
            self.stamina = self.max_stamina

    def use_stamina(self, amount: int) -> bool:
        if (self.stamina - amount) >= 0:
            self.stamina -= amount
            return True
        else:
            return False
        