from blessed import Terminal
from random import randint
from .terminal_entity import TerminalEntity


class Food(TerminalEntity):
    def __init__(self, term: Terminal, sprite: str) -> None:
        super().__init__(term, sprite)
        self.spawn()
        self.speed = 6
        self.set_target_xy(int(self.position_x), term.height-15)
    
    def spawn(self):
        x = randint(10, self.term.width - self.sprite_width-25)
        y = randint(0, 5)
        self.update_position_xy(x, y)
    
    


    
