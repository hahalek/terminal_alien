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
        self.sprite_width = len(self.sprite_right.splitlines()[1])
        self.sprite_height = len(self.sprite_right.splitlines())
        self.position_x = 0
        self.head_x = self.position_x + self.sprite_width
        self.position_y = 0
        self.x0 = self.position_x
        self.y0 = self.position_y
        self.target_x = self.position_x
        self.target_y = self.position_y
        self.speed = 4
        self.at_target = True
        self.turned_right = True
        logging.info(f"sprite dimentions: {self.sprite_width}, {self.sprite_height}")
        logging.info(f"entity position: {self.position_x}, {self.position_y}")

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
        if self.turned_right:
            self.head_x = self.position_x + self.sprite_width
        else:
            self.head_x = self.position_x
        self.position_y = y

    def get_position_int(self):
        return int(self.position_x), int(self.position_y)

    def set_target_xy(self, x: int, y: int):
        self.target_x = x
        self.target_y = y

        if self.turned_right == False and self.target_x > self.head_x + int(self.sprite_width/2):
            self.turned_right = True
            self.active_sprite = self.sprite_right
            self.head_x = self.position_x + self.sprite_width
        elif self.turned_right == True and self.target_x < self.head_x - int(self.sprite_width/2):
            self.turned_right = False
            self.active_sprite = self.sprite_left
            self.head_x = self.position_x

        self.x0 = self.head_x
        self.y0 = self.position_y
        logging.info(f"x0, y0 zaraz po przypisaniu: {self.x0, self.y0}")
        logging.info(f"position zaraz po przypisaniu: {self.position_x, self.position_y}")
        logging.info(f"head zaraz po przypisaniu: {self.head_x, self.position_y}")
        logging.info(f"target zaraz po przypisaniu: {self.target_x, self.target_y}")
        logging.info(f" ")

        self.at_target = False

    def set_speed(self, speed: float):
        self.speed = speed

    def move(self):
        if not self.at_target:            
            # if self.target_x >= self.position_x:
            #     self.active_sprite = self.sprite_right
            # else:
            #     self.active_sprite = self.sprite_left
            dx = self.target_x - self.x0
            dy = self.target_y - self.y0
            L = sqrt(pow((dx), 2) + pow(dy, 2))
            self.position_x += self.speed * dx/L * 1/FPS
            self.position_y += self.speed * dy/L * 1/FPS
            
            self.position_x = max(0, self.position_x)
            self.position_y = max(0, self.position_y)

            self.position_x = min(self.position_x, self.term.width - self.sprite_width - 15)
            self.position_y = min(self.position_y, self.term.height - self.sprite_height - 2)
            if self.turned_right:
                self.head_x = self.position_x + self.sprite_width
            else:
                self.head_x = self.position_x
            logging.info(f"head_x = {self.head_x}")
            logging.info(f"x0, y0 = {self.x0, self.y0}, target = {self.target_x, self.target_y}, dx, dy = {self.speed * dx/L * 1/FPS, self.speed * dy/L * 1/FPS}")

            if abs(self.position_y - self.target_y) < 2 and abs(self.head_x - self.target_x) < 2:
                self.at_target = True
