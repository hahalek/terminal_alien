import logging
from time import sleep
from random import uniform
from blessed import Terminal
from modules.shrimp import Shrimp
from modules.sprites import shrimp_sprite, plant_sprite, fish_sprite, food_sprite
from modules.terminal_entity import TerminalEntity
from modules.printer import Printer
from modules.food import Food
from GLOBALS import FPS


logging.basicConfig(
    filename="app.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

term = Terminal()



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

    with term.cbreak():
        key = term.inkey(timeout=1/FPS)
        if key == ' ':
            food = Food(term, food_sprite)
            entities.append(food)


    for entity in entities:
        entity.move()
    printer.update_all(entities)
    printer.print()
