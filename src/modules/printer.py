import logging
from time import sleep
from random import uniform
from blessed import Terminal
from modules.shrimp import Shrimp
from modules.sprites import shrimp_sprite, plant_sprite, fish_sprite
from modules.terminal_entity import TerminalEntity
from GLOBALS import FPS


class Printer():
    def __init__(self, term: Terminal) -> None:
        self.term = term
        self.display = (' ' * term.width + '\n') * (term.height - 1)
        self.empty = self.display

    def update_char_at(self, x: int, y: int, char: str):
        lines = self.display.splitlines()
        line = lines[y]
        lines[y] = line[:x] + char + line[x + 1:]
        self.display = '\n'.join(lines)

    def print(self):
        print(self.display)

    def clear(self):
        self.display = self.empty

    def update_entity(self, entity: TerminalEntity):
        y = entity.position_y
        x = entity.position_x
        sprite_lines = entity.active_sprite.splitlines()
        for line in sprite_lines:
            for char in line:
                if char == ' ':
                    x += 1
                elif char == 'a':
                    self.update_char_at(int(x), int(y), ' ')
                    x += 1
                else:
                    self.update_char_at(int(x), int(y), char)
                    x += 1
            x = entity.position_x
            y += 1
    
    def update_all(self, entities: list[TerminalEntity]):
        for entity in entities:
            self.update_entity(entity)