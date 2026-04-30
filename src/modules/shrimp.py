import logging
from random import randint, uniform
from blessed import Terminal
from .terminal_entity import TerminalEntity
from .food import Food
from GLOBALS import FPS


class Shrimp(TerminalEntity):
    def __init__(self, term: Terminal, sprite: str) -> None:
        super().__init__(term, sprite)
        self.has_target = False
        self.target_timer = float("+inf")
        self.chasing_food = False
    
    def decide_on_target(self, timer: float):
        if self.target_timer < timer:
            self.target_timer += 1/FPS
        else:
            self.target_timer = 0
            x = randint(0, self.term.width - self.sprite_width-2)
            y = randint(0, self.term.height - self.sprite_height-2)
            logging.info(f"position = {self.position_x, self.position_y}, to_right = {self.turned_right}")
            logging.info(f"NEW TARGET = {x, y}")
            self.speed = uniform(0.01, 10)
            self.set_target_xy(x, y)
            self.target_timer += 1/FPS
    
    def detecting_food(self, food: Food):
        if min(abs(self.position_x - food.position_x), abs(self.position_x + self.sprite_width - food.position_x)) < 60 and abs(self.position_y - food.position_y) < 15:
            self.speed = 50
            self.chasing_food = True
            return True
        self.chasing_food = False
        return False