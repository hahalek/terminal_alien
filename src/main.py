from time import sleep
from random import uniform
from blessed import Terminal
from shrimp import Shrimp
from sprite import sprite


term = Terminal()
shrimp = Shrimp(term, sprite)
shrimp.print_at(3, 3)
while True:
    shrimp.go_to(int(uniform(0, term.width-23)/2), int(uniform(0, term.height-12)), uniform(1.8, 5))