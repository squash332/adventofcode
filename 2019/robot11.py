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

panels = defaultdict(int)
visited_locations = set ()
DIRECTIONS = [Position(-1, 0), Position(0, 1), Position(1, 0), Position(0, -1)] # 0,1,2,3, UP, RIGHT, DOWN, LEFT
direction = 0
computer = op.IntCode(arr)
position = Position(0,0)
# panels[robot] = color 1st output paint 2nd output turn direction then move forwards

counter = 0
while True:
    color = panels[position]
    computer.inputs.append(color)
    visited_locations.add(position)

    if computer.run():
        break
    # if(len(computer.result) == 0):
    #     break
    paint = computer.result.pop()
    counter += 1

    computer.run()
    # if(len(computer.result) == 0):
    #     break
    turn = computer.result.pop()

    

    panels[position] = paint
    if turn == 0:
        direction = (direction -1) % 4
    else:
        direction = (direction +1) % 4
    position = position + DIRECTIONS[direction]

print(len(visited_locations))








