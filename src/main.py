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

animals = [shrimp1, shrimp2, shrimp3, fish]
entities = [plant1, plant2, shrimp1, shrimp2, shrimp3, fish]


shrimp1.update_position_xy(0, 0)
shrimp2.update_position_xy(105, 6)
shrimp3.update_position_xy(13, 30)
fish.update_position_xy(70, 30)
plant1.update_position_xy(15, 26)
plant2.update_position_xy(150, 22)
foods = []


# MAKE FISH NOT EAT FOOD WITH THEIR ASS bug

while True:
    printer.clear()

    with term.cbreak():
        key = term.inkey(timeout=1/FPS)
        if key == ' ':
            food = Food(term, food_sprite)
            entities.append(food)
            foods.append(food)

    for animal in animals:
        if foods:
            for food in foods:
                if animal.detecting_food(food):
                    animal.set_target_xy(food.position_x, food.position_y)
                if min(abs(animal.position_x - food.position_x), abs(animal.position_x + animal.sprite_width - food.position_x)) < 2 and  food.position_y - animal.position_y < 5:
                    logging.info(f"food to delete: {food}")
                    logging.info(f"Deleting from: {entities}")
                    if food in entities:
                        animal.chasing_food = False
                        entities.remove(food)
                        foods.remove(food)
                        del food
                        animal.speed = uniform(0.01, 10)
        else:
            animal.chasing_food = False

    for animal in animals:
        if animal.chasing_food == False:
            animal.decide_on_target(timer = uniform(0.1,  20))
    for entity in entities:
        entity.move()

    printer.update_all(entities)
    # for animal in animals:
        # printer.update_char_at(int(animal.position_x), int(animal.position_y), 'v')
        # printer.update_char_at(int(animal.head_x), int(animal.position_y), 'X')
        # printer.update_char_at(int(animal.target_x), int(animal.target_y), 'T')
        # printer.update_char_at(int(animal.x0), int(animal.y0), 's')

    printer.print()
