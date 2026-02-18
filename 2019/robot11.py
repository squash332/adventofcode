# robot needs to move around on grid of square panels
# robot detects the color of current panel and paints it black or white

# all of the panels are currently black

# provide 0 if robot over black panel or 1 if robot over a white panel

# output:
# first: it will output value indicating the color to paint the panel
#     0 means to paint the panel black, 1 means paint it white
# second: it will output a value indicating the direction the robot should turn
#     0 means it should turn left 90 degrees, 1 means turn right 90 degrees

# after robot turns it should move forward 1 panel
# robot starts facing up
from collections import defaultdict
from dataclasses import dataclass
import opcode2 as op
from opcode2 import arr


@dataclass(frozen=True)
class Position:
    x: int
    y: int
    
    def __add__(self, other: "Position") -> "Position":
        return Position(self.x + other.x, self.y + other.y)


DIRECTIONS = [Position(-1, 0), Position(0, 1), Position(1, 0), Position(0, -1)] # 0,1,2,3, UP, RIGHT, DOWN, LEFT
computer = op.IntCode(arr)
panels = defaultdict(lambda:0)

def start_painting():
    direction = 0
    position = Position(0,0)
    panels[position] = 1
    print(panels)
    while True:
        color = panels[position]

        computer.inputs.append(color)
        if computer.run():
            break

        paint = computer.result.pop()
        computer.run()
        turn = computer.result.pop()

        panels[position] = paint
        
        if turn == 0:
            direction = (direction -1) % 4
        else:
            direction = (direction +1) % 4
        position = position + DIRECTIONS[direction]
    return len(panels)
    

# result = start_painting()
# for k,v in panels.items():
#         print(k,v)
# print(result)


#p2

test = panels.get(Position(4, 39))
print("*************************", test)

registration_identifier = [[' ']*45 for i in range(6)]
for row in range(6):
    for col in range(45):
        if panels.get(Position(row, col)) == 1:
            registration_identifier[row][col] = 'I'
        else:
            registration_identifier[row][col] = '.'

for row in registration_identifier:
    print(''.join(row))










