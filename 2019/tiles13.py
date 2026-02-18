import opcode2 as op
from opcode2 import arr
from enum import Enum
from dataclasses import dataclass

@dataclass 
class Position:
    x: int
    y: int

    def __add__(self, other: "Position") -> "Position":
        return Position(self.x + other.x, self.y + other.y)
    
DIRECTIONS = [Position(-1, 1), # top left 
              Position(1, 1),  # top right
              Position(-1, -1),  # bottom left
              Position(1, -1)] # bottom right

TILES = {
    
}

computer = op.IntCode(arr)
counter = 0
while True:
    computer.run()
    computer.result.pop(0)
    computer.run()
    computer.result.pop(0)
    computer.run()

    block_id = computer.result.pop(0)
    if block_id == 2:
        counter += 1

    if computer.run():
        break
print("printing results:", counter)