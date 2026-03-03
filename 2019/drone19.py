from collections import defaultdict
from dataclasses import dataclass
import opcode2 as op
from opcode2 import arr


def get_grid(x,y):
    values = iter([x,y])
    return lambda: next(values)


def beam(x,y):
    computer = op.IntCode(arr, get_grid(x,y))
    return computer.run()

x = 0
grid = {}
y = 500

while True:
    while beam(x,y) == 0:
        x += 1
        
    # if (x, y) not in grid:
    #     grid[(x,y)] = beam(x,y)
        
    # bottom left x,y 
    # top right x + 99 y - 99

    #print top left (closest) x, y - 99
    if beam(x + 99,y - 99) == 1:
        x,y = x, y-99
        break
    y += 1

print("part 2 =", x*10000 + y)

    