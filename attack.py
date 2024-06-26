from effect import Effect
from entity import Entity

class Attack:
    def __init__(self, dmg: int, cost: int, effects: dict[str, Effect]=None) -> None:
        self.dmg = dmg
        self.cost = cost
        self.effects = effects
        self.duration = 0
        if self.effects is not None and len(self.effects) != 0:
            for value in self.effect.values():
                if value.duration > self.duration:
                    self.duration = value.duration
    
    def has_effects(self) -> bool:
        return (self.effects is not None and len(self.effects) != 0)
    
    def damage(self, target: Entity):
        target.damage(dmg)
    
    def apply_effects(self, target: Entity, delta: int) -> None:
        self.duration -= delta
        if self.duration < 0:
            self.duration = 0
        for key, value in self.effects.items():
            if value.is_finished():
                del self.effects[key]
            else:
                value.damage(target, delta)
                if value.is_finished():
                    del self.effects[key]