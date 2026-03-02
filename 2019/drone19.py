from collections import defaultdict

import opcode2 as op
from opcode2 import arr

def get_grid(x,y):
    values = iter([x,y])
    return lambda: next(values)

def draw_grid():
    counter = 0
    for x in range(50):
        row = ""
        for y in range(50):
            match grid[(x,y)]:
                case 1:
                    row += "#"
                    counter += 1
                case 0:
                    row += "."

        print(row)
    return counter


grid = {}
for x in range(50):
    for y in range(50):
        computer = op.IntCode(arr, get_grid(x,y))
        result = computer.run()
        grid[(x,y)] = result


print("part 1:", draw_grid())
    