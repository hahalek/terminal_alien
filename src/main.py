from time import sleep
from blessed import Terminal


term = Terminal()

# # reading keystrokes from terminal
# term = Terminal()
# with term.cbreak():
#     key = term.inkey()
#     print(f"You pressed: {key!r}")


# shrimp_string = r"""
#     ______________
#     ____________  \
#                 \ |
#                 / /
#      /=========== * ===
#     /=============-----
#    /=============\\
#   // |||| }}\\\\
#   |||
#    \\\
#     \\\ """

class Shrimp():
    def __init__(self, sprite_string: str) -> None:
        self.sprite = sprite_string
        self.position_x = 0
        self.position_y = 0
        
    def print_at(self, x: int, y: int, wait: float = 0.3, reverse: bool = False) -> None:
        print(term.clear, end='')
        if reverse:
            for line in self.sprite.splitlines():
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
                    
                print(term.move_xy(x, y), ' '*x + new_line[::-1], end=' ')
                y += 1
        else:
            for line in self.sprite.splitlines():
                print(term.move_xy(x, y), ' '*x + line, end='')
                y += 1
        print(sleep(wait))
        

    # def print_at_reverse(self, x: int, y: int, wait: float = 0.3)  -> None:
    #     print(term.clear, end=' ')
    #     for line in self.sprite.splitlines():
    #         new_line = ""
    #         for char in line:
    #             if char == r"/":
    #                 new_line += "\\"
    #             elif char == "\\":
    #                 new_line += r"/"
    #             elif char == r"}":
    #                 new_line += r"{"
    #             else:
    #                 new_line += char
                
    #         print(term.move_xy(x, y), ' '*x + new_line[::-1], end=' ')
    #         y += 1
    #     print(sleep(wait))


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

shrimp = Shrimp(sprite)
shrimp.print_at(0, 0,  2, True)
shrimp.print_at(5, 5, 2, True)
shrimp.print_at(10, 10, 2)
shrimp.print_at(15, 15, True)
shrimp.print_at(20, 14, 2)
shrimp.print_at(23, 18, True)
shrimp.print_at(28, 16)
shrimp.print_at(32, 19)