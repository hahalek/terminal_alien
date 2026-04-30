import logging
from random import randint
from random import uniform
from blessed import Terminal
from modules.shrimp import Shrimp
from modules.sprites import shrimp_sprite, plant_sprite, fish_sprite, food_sprite, grass1_sprite, grass2_sprite
from modules.terminal_entity import TerminalEntity
from modules.printer import Printer
from modules.food import Food
from GLOBALS import FPS

grass_sprites = [grass1_sprite, grass2_sprite]

logging.basicConfig(
    filename="app.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

term = Terminal()



printer = Printer(term)

animals = []
entities = []

for i in range(randint(15, 25)):
    grass = TerminalEntity(term, grass_sprites[randint(0, len(grass_sprites)-1)])
    grass.update_position_xy(randint(2, term.width-grass.sprite_width-2), randint(int((term.height-grass.sprite_height)*3/4), term.height-grass.sprite_height-2))
    entities.append(grass)

for i in range(randint(0, 2)):
    plant = TerminalEntity(term, plant_sprite)
    plant.update_position_xy(randint(2, term.width-plant.sprite_width-2), randint(int((term.height-plant.sprite_height)*2/3), term.height-plant.sprite_height-2))
    entities.append(plant)

for i in range(randint(1, 2)):
    shrimp = Shrimp(term, shrimp_sprite)
    shrimp.update_position_xy(randint(2, term.width-shrimp.sprite_width-2), randint(0, term.height-shrimp.sprite_height-2))
    animals.append(shrimp)
    entities.append(shrimp)

for i in range(randint(1, 3)):
    fish = Shrimp(term, fish_sprite)
    fish.update_position_xy(randint(2, term.width-fish.sprite_width-2), randint(0, term.height-fish.sprite_height-2))
    animals.append(fish)
    entities.append(fish)

foods = []


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
                if abs(animal.head_x - food.position_x) < 2 and 0 <= food.position_y - animal.position_y < 5:
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
    printer.print()
