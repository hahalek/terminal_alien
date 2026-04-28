import logging
from math import sqrt, pow
from time import sleep
from blessed import Terminal
from GLOBALS import FPS


# class Printer():
#     def __init__(self, term: Terminal) -> None:
#         self.term = term
#         self.entities = []

#     def add_entity(self, entity):
#         self.entities.append(entity)
    
#     def remove_entity(self, the_entity):
#         new_list = []
#         for entity in self.entities:
#             if entity is not the_entity:
#                 new_list.append(entity)
#         self.entities = new_list
    
#     def print_all(self, fps: int):
#         print(self.term.clear, end='')
#         for entity in self.entities:
#             entity.print()
#         sleep(1/fps)



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
            # dx = 0
            # dy = 0
            # if self.target_x - self.x0 != 0:
            #     dx = self.speed * cos(atan((self.target_y - self.y0)/(self.target_x - self.x0))) * 1/FPS
            # if self.target_y - self.y0 != 0:
            #     dy = self.speed * sin(atan((self.target_y - self.y0)/(self.target_x - self.x0))) * 1/FPS
            
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

            self.position_x = min(self.position_x, self.term.width - len(self.sprite_right.splitlines()[0])-2)
            self.position_y = min (self.position_y, self.term.height - len(self.sprite_right.splitlines())-2)

            logging.info(f"y0 = {self.y0}, target y = {self.target_y}, dy = {self.speed * dy/L * 1/FPS}")
            # if self.target_x >= self.position_x:
            #     self.position_x += dx
            #     self.active_sprite = self.sprite_right
            # else:
            #     self.position_x -= dx
            #     self.active_sprite = self.sprite_left
            # if self.target_y >= self.position_y:
            #     self.position_y += dy
            #     logging.info(f"dy = +{dy}")
            # else:
            #     self.position_y -= dy
            #     logging.info(f"dy = -{dy}")
            if abs(self.position_x - self.target_x) < 1:
                self.at_target = True


        


    # def print(self):
    #     x = self.position_x
    #     y = self.position_y
    #     for line in self.sprite.splitlines():
    #         if self.reversed:
    #             line = self.get_reversed_line(line)
    #         print(self.term.move_xy(x, y), line, end=' ')
    #         y += 1
    




    # def print_at(self, x: int, y: int, wait: float = 0, reverse: bool = False) -> None:
    #     self.position_x = x
    #     self.position_y = y
    #     for line in self.sprite.splitlines():
    #         if reverse:
    #             line = self.get_reversed_line(line)
    #         print(self.term.move_xy(x, y), line, end=' ')
    #         y += 1
    #     sleep(wait)
    #     print('')

    # def move_to(self, x: int, y: int, wait: float = 0, reverse: bool = False) -> None:
    #     self.print_at(self.position_x + x,
    #                   self.position_y + y,
    #                   wait,
    #                   reverse)
    
    # def go_to(self, x1: int, y1: int, time: float = 1) -> None:
    #     """
    #     Make an entity go to a specified place in specified time in straight line.
    #     """
    #     x0 = self.position_x
    #     y0 = self.position_y
    #     reverse = False
    #     if x1 - self.position_x < 0:
    #         reverse = True
    #     if abs(self.position_x - x1) >= abs(self.position_y - y1):
    #         number_of_stpes = abs(self.position_x - x1)
    #     else:
    #         number_of_stpes = abs(self.position_y - y1)
    #     number_of_stpes = max(number_of_stpes, 10)
    #     dt = time/number_of_stpes

    #     x_path = []
    #     y_path = []
    #     for i in range(number_of_stpes):
    #         x_path.append(round(x0 + (i+1)*(x1 - self.position_x)/number_of_stpes))
    #         y_path.append(round(y0 + (i+1)*(y1 - self.position_y)/number_of_stpes))
        
    #     for i in range(len(x_path)):
    #         self.print_at(x_path[i], y_path[i], dt, reverse)