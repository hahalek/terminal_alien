from time import sleep
from random import uniform
from blessed import Terminal
from modules.shrimp import Shrimp
from modules.sprites import shrimp_sprite, plant_sprite
from modules.terminal_entity import TerminalEntity


term = Terminal()
shrimp = Shrimp(term, shrimp_sprite)
plant = TerminalEntity(term, plant_sprite)
shrimp.print_at(3, 3)
while True:
    print(term.clear, end='')
    plant.print_at(14, 27)
    shrimp.go_to(int(uniform(0, term.width-23)/2), int(uniform(0, term.height-12)), uniform(1.8, 5))
    