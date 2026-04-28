from time import sleep
from random import randint, uniform
from blessed import Terminal
from .terminal_entity import TerminalEntity
from GLOBALS import FPS


class Shrimp(TerminalEntity):
    def __init__(self, term: Terminal, sprite: str) -> None:
        super().__init__(term, sprite)
        self.has_target = False
        self.target_timer = 0
    
    def decide_on_target(self, time: float):
        if self.target_timer < time:
            self.target_timer += 1/FPS
        else:
            self.target_timer = 0
            x = randint(0, self.term.width - len(self.sprite_right.splitlines()[0])-2)
            y = randint(0, self.term.height - len(self.sprite_right.splitlines())-2)
            # print(f"{__file__} Max random y = {len(self.sprite_right.splitlines())-2}")
            self.speed = uniform(0.1, 15)
            self.set_target_xy(x, y)
            self.target_timer += 1/FPS