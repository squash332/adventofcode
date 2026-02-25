from collections import defaultdict
from dataclasses import dataclass

import opcode2 as op
from opcode2 import arr

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    
    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)




def output(pos):
    # print(pos)

    scaffolds = set ()
    robot = set ()
    
    grid = ''.join(chr(x) for x in pos )
    # print(grid)
    lines = grid.strip().split('\n')

    for r, row in enumerate(lines):
        for c, ch in enumerate(row):
            if ch == '#':
                scaffolds.add((r,c))
            if ch == "^":
                robot.add((r,c))
            
    # print(scaffolds)
    # print((1,0) in scaffolds)
    # print(pos)
    # print(robot)

    return scaffolds

def find_intersections(scaffolds):

    sum = 0
    for x in scaffolds:
        # print("BALBLAB", x, type(x))
        position = Point(*x)
        neighbours = []
        for direction in [1,2,3,4]:
            next_position = position + DIRECTIONS[direction]
            # print(position, next_position)  point = point +

            if (next_position.x, next_position.y) in scaffolds:
                neighbours.append(next_position)
                # print("waaaaaaaaaaaa", neighbours)
            else:
                continue
        if len(neighbours) == 4:
            # print("intersection at:", position)
            sum += position.x * position.y
    print("part 1:", sum)
    
computer = op.IntCode(arr, lambda:None)

DIRECTIONS = {
    1: Point(0, 1),   # up
    2: Point(0, -1),  # down
    3: Point(-1, 0),  # left
    4: Point(1, 0)    # right
    } 
rows = 0
flag = False
columns = 0
pos = []

while True:

    element = computer.run()
    if element == None:
        break
    pos.append(element)
    
    # if element != 10 and not f#lag:
    #     columns += 1

    # if element == 10:
    #     flag = True
    #     rows += 1



# print(f"rows: , {rows + 1}, columns :{columns}")
scaffolds = output(pos)
find_intersections(scaffolds)





