import logging
from random import randint, uniform
from blessed import Terminal
from .terminal_entity import TerminalEntity
from GLOBALS import FPS


class Shrimp(TerminalEntity):
    def __init__(self, term: Terminal, sprite: str) -> None:
        super().__init__(term, sprite)
        self.has_target = False
        self.target_timer = 0
    
    def decide_on_target(self, timer: float):
        if self.target_timer < timer:
            self.target_timer += 1/FPS
        else:
            self.target_timer = 0
            x = randint(0, self.term.width - len(self.sprite_right.splitlines()[0])-2)
            y = randint(0, self.term.height - len(self.sprite_right.splitlines())-2)
            logging.info(f"NEW TARGET = {y}")
            self.speed = uniform(0.01, 30)
            self.set_target_xy(x, y)
            self.target_timer += 1/FPS