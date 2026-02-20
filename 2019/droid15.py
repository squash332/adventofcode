import opcode2 as op
from opcode2 import arr
from dataclasses import dataclass
import ctypes

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

# accept movement command via input instruction
def movement_command():
    movements = ["1","2","3","4"]

    while True:
        user_input = input("enter 1,2,3 or 4: ")
    
        if user_input in movements:
            chosen_number = int(user_input)
            break
    return chosen_number

# def paint(reply):



computer = op.IntCode(arr, movement_command)
DIRECTIONS = {
    1: Point(0, 1),   # north
    2: Point(0, -1),  # south
    3: Point(-1, 0),  # west
    4: Point(1, 0)    # east
    } 

position = Point(0,0)
map_grid = {} # (0,0) = je D

while True:
    reply = computer.run()
    print("CHOSEN NUMBER:", computer.inputs())
    print("REPLY: ", reply)
    # paint(reply)
    


    