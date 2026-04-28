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
        x = entity.position_x
        y = entity.position_y
        sprite_lines = entity.sprite.splitlines()
        for line in sprite_lines:
            for char in line:
                if char == ' ':
                    x += 1
                else:
                    self.update_char_at(int(x), int(y), char)
                    x += 1
            x = entity.position_x
            y += 1
    
    def update_all(self, entities: list[TerminalEntity]):
        for entity in entities:
            self.update_entity(entity)
    

printer = Printer(term)
shrimp1 = TerminalEntity(term, shrimp_sprite)
# shrimp2 = TerminalEntity(term, shrimp_sprite)
plant = TerminalEntity(term, plant_sprite)
entities = [plant, shrimp1]

# printer.update_char_at(5, 29, 'G')
# printer.update_char_at(6, 29, 'o')
# printer.update_char_at(7, 29, 'w')
# printer.update_char_at(8, 29, 'n')
# printer.update_char_at(9, 29, 'o')


shrimp1.update_position_xy(2, 2)
# shrimp2.update_position_xy(43, 23)
plant.update_position_xy(4, 4)
shrimp1.set_target_xy(30, 20)

while True:
    printer.clear()
    for entity in entities:
        entity.move()
    printer.update_all(entities)
    printer.print()
    sleep(1/60)

# shrimp = Shrimp(term, shrimp_sprite)
# plant = TerminalEntity(term, plant_sprite)
# shrimp.print_at(3, 3)
# while True:
#     print(term.clear, end='')
#     plant.print_at(14, 27)
#     shrimp.go_to(int(uniform(0, term.width-23)/2), int(uniform(0, term.height-12)), uniform(1.8, 5))
    