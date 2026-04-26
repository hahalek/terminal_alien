from time import sleep
from blessed import Terminal
from .terminal_entity import TerminalEntity


class Shrimp(TerminalEntity):
    def __init__(self, term: Terminal, sprite: str) -> None:
        super().__init__(term, sprite)
        self.position_x = 0
        self.position_y = 0
        self.terminal_x = self.term.width
        self.terminal_y = self.term.height
