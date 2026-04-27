from time import sleep
from random import uniform
from blessed import Terminal
from modules.shrimp import Shrimp
from modules.sprites import shrimp_sprite, plant_sprite
from modules.terminal_entity import TerminalEntity


term = Terminal()

class Printer():
    def __init__(self, term: Terminal) -> None:
        self.term = term
        self.display = (' ' * term.width + '\n') * (term.height - 1)

    def update_char_at(self, x: int, y: int, char: str):
        lines = self.display.splitlines()
        line = lines[y]
        lines[y] = line[:x] + char + line[x + 1:]
        self.display = '\n'.join(lines)

    def print(self):
        print(self.display)

    def clear(self):
        print(self.term.clear, end='')

    def update_entity(self, entity: TerminalEntity):
        x = entity.position_x
        y = entity.position_y
        sprite_lines = entity.sprite.splitlines()
        for line in sprite_lines:
            for char in line:
                if char == ' ':
                    x += 1
                else:
                    self.update_char_at(x, y, char)
                    x += 1
            x = entity.position_x
            y += 1
    

printer = Printer(term)
shrimp = TerminalEntity(term, shrimp_sprite)
printer.update_char_at(5, 29, 'G')
printer.update_char_at(6, 29, 'o')
printer.update_char_at(7, 29, 'w')
printer.update_char_at(8, 29, 'n')
printer.update_char_at(9, 29, 'o')
shrimp.update_position_x(8)
shrimp.update_position_y(20)
printer.update_entity(shrimp)
printer.print()

# shrimp = Shrimp(term, shrimp_sprite)
# plant = TerminalEntity(term, plant_sprite)
# shrimp.print_at(3, 3)
# while True:
#     print(term.clear, end='')
#     plant.print_at(14, 27)
#     shrimp.go_to(int(uniform(0, term.width-23)/2), int(uniform(0, term.height-12)), uniform(1.8, 5))
    