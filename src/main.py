from time import sleep
from blessed import Terminal


term = Terminal()



class Shrimp():
    def __init__(self, term: Terminal, sprite_string: str) -> None:
        self.term = term
        self.sprite = sprite_string
        self.position_x = 0
        self.position_y = 0
        self.terminal_x = term.width
        self.terminal_y = term.height

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

    def print_at(self, x: int, y: int, wait: float = 0.3, reverse: bool = False) -> None:
        self.position_x = x
        self.position_y = y
        print(self.term.clear, end='')
        for line in self.sprite.splitlines():
            if reverse:
                line = self.get_reversed_line(line)
            print(self.term.move_xy(x, y), ' '*x + line, end=' ')
            y += 1
        sleep(wait)
        print('')

    def move_to(self, x: int, y: int, wait: float = 0.3, reverse: bool = False) -> None:
        self.print_at(self.position_x + x,
                      self.position_y + y,
                      wait,
                      reverse)
    
    def go_to(self, x1: int, y1: int, time: float = 1) -> None:
        """
        Make a shrimp go to a specified place in specified time in straight line.
        """
        x0 = self.position_x
        y0 = self.position_y
        reverse = False
        if x1 - self.position_x < 0:
            reverse = True
        if abs(self.position_x - x1) >= abs(self.position_y - y1):
            number_of_stpes = abs(self.position_x - x1)
        else:
            number_of_stpes = abs(self.position_y - y1)
        number_of_stpes = max(number_of_stpes, 10)
        dt = time/number_of_stpes

        x_path = []
        y_path = []
        for i in range(number_of_stpes):
            x_path.append(round(x0 + (i+1)*(x1 - self.position_x)/number_of_stpes))
            y_path.append(round(y0 + (i+1)*(y1 - self.position_y)/number_of_stpes))
        
        for i in range(len(x_path)):
            self.print_at(x_path[i], y_path[i], dt, reverse)


sprite = r"""A
  ______________      
  ____________  \     
              \ |     
              / /     
   /=========== * === 
  /=============----- 
 /=============\\     
// |||| }}\\\\        
|||                   
 \\\                  
  \\\                 """

shrimp = Shrimp(term, sprite)
shrimp.print_at(3, 3)
shrimp.go_to(23, 19, 3)
shrimp.go_to(32, 8, 3)
shrimp.go_to(33, 9, 3)
shrimp.go_to(8, 14, 5)