import logging
from time import sleep
from random import uniform
from blessed import Terminal
from modules.shrimp import Shrimp
from modules.sprites import shrimp_sprite, plant_sprite, fish_sprite
from modules.terminal_entity import TerminalEntity
from GLOBALS import FPS


logging.basicConfig(
    filename="app.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

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
    

printer = Printer(term)
shrimp1 = Shrimp(term, shrimp_sprite)
shrimp2 = Shrimp(term, shrimp_sprite)
shrimp3 = Shrimp(term, shrimp_sprite)
fish = Shrimp(term, fish_sprite)

plant1 = TerminalEntity(term, plant_sprite)
plant2 = TerminalEntity(term, plant_sprite)

shrimps = [shrimp1, shrimp2, shrimp3, fish]
entities = [plant1, plant2, shrimp1, shrimp2, shrimp3, fish]


shrimp1.update_position_xy(3, 2)
shrimp2.update_position_xy(105, 6)
shrimp3.update_position_xy(13, 30)
fish.update_position_xy(70, 30)
plant1.update_position_xy(15, 26)
plant2.update_position_xy(150, 22)


# print(term.does_mouse())

# print("Click anywhere! ^C to quit")
# with term.cbreak(), term.mouse_enabled():
#     while True:
#         inp = term.inkey()
#         if inp.name and inp.name.startswith('MOUSE_'):
#             print(f"button {inp.name} at (y={inp.mouse_yx})")        # USE KITTY TERMINAL

while True:
    printer.clear()
    for shrimp in shrimps:
        logging.info(f"{shrimp.position_y} --> {shrimp.target_y}")
        shrimp.decide_on_target(timer = uniform(0.1,  20))


    for entity in entities:
        entity.move()
    printer.update_all(entities)
    printer.print()
    sleep(1/FPS)
