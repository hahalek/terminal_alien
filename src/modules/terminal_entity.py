import logging
from math import sqrt, pow
from blessed import Terminal
from GLOBALS import FPS


class TerminalEntity():
    def __init__(self, term: Terminal, sprite: str) -> None:
        self.term = term
        self.active_sprite = sprite
        self.sprite_right = sprite
        self.sprite_left = self.turn_sprite_left()
        self.position_x = 0
        self.position_y = 0
        self.x0 = 0
        self.y0 = 0
        self.target_x = 0
        self.target_y = 0
        self.speed = 4
        self.at_target = True

    def get_reversed_line(self, line: str) -> str:
        new_line = ""
        for char in line:
            if char == r"/":
                new_line += "\\"
            elif char == "\\":
                new_line += r"/"
            elif char == r"}":
                new_line += r"{"
            elif char == r"(":
                new_line += r")"
            elif char == r")":
                new_line += r"("
            else:
                new_line += char
        return new_line[::-1]

    def turn_sprite_left(self):
        sprite_left = ''
        for line in self.sprite_right.splitlines():
            sprite_left += self.get_reversed_line(line) + "\n"
        return sprite_left

    def update_position_x(self, x: int):
        self.position_x = x
    
    def update_position_y(self, y: int):
        self.position_y = y

    def update_position_xy(self, x: int, y: int):
        self.position_x = x
        self.position_y = y

    def set_target_xy(self, x: int, y: int):
        self.target_x = x
        self.target_y = y
        self.x0 = self.position_x
        self.y0 = self.position_y
        self.at_target = False
    
    def set_speed(self, speed: float):
        self.speed = speed

    def move(self):
        if not self.at_target:            
            if self.target_x >= self.position_x:
                self.active_sprite = self.sprite_right
            else:
                self.active_sprite = self.sprite_left
            dx = self.target_x - self.x0
            dy = self.target_y - self.y0
            L = sqrt(pow((dx), 2) + pow(dy, 2))
            self.position_x += self.speed * dx/L * 1/FPS
            self.position_y += self.speed * dy/L * 1/FPS
            
            self.position_x = max(0, self.position_x)
            self.position_y = max(0, self.position_y)

            self.position_x = min(self.position_x, self.term.width - len(self.sprite_right.splitlines()[0])-10)
            self.position_y = min(self.position_y, self.term.height - len(self.sprite_right.splitlines())-2)

            logging.info(f"y0 = {self.y0}, target y = {self.target_y}, dy = {self.speed * dy/L * 1/FPS}")

            if abs(self.position_y - self.target_y) < 1:
                self.at_target = True
