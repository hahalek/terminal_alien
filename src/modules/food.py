from blessed import Terminal
from random import randint
from .terminal_entity import TerminalEntity



class Food(TerminalEntity):
    def __init__(self, term: Terminal, sprite: str) -> None:
        super().__init__(term, sprite)
        self.spawn()
        self.speed = 8
        self.set_target_xy(int(self.position_x), term.height-10)
    
    def spawn(self):
        x = randint(0, self.term.width - len(self.sprite_right.splitlines()[0])-2)
        y = randint(0, 5)
        self.update_position_xy(x, y)
    


    
