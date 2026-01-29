  
#   ....#.....      ....#.....
#   .........#      ....XXXXX#
#   ..........      ....X...X.              41 distinct positions
#   ..#.......      ..#.X...X.
#   .......#..      ..XXXXX#X.
#   ..........      ..X.X.X.X.
#   .#..^.....      .#XXxXXXX.
#   ........#.      .XXXXXXX#.
#   #.........      #XXXXXXX..
#   ......#...      ......#X.. 

# ^ - guard's starting position
# # - obstacles, when obstacle is in front of guard : stop, turn right 90° and then keep moving
# - guard is moving 1 step at a time
# - need to count unique moves until guard leaves mapped area


from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def up(self):
        return Point(self.x - 1, self.y)
    
    def right(self):
        return Point(self.x, self.y + 1)
    
    def down(self):
        return Point(self.x + 1, self.y)
    
    def left(self):
        return Point(self.x, self.y - 1)

from pathlib import Path

input_str = Path(__file__).parent / "pathing.txt"
# data = str(input_str.read_text().strip().splitlines())
arr = []

DIRECTION = {
    "up": Point.up,
    "right": Point.right,
    "down": Point.down,
    "left":Point.left
}

TURN_RIGHT = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up"
}

guard = set()
obstacle = set()

for r, line in enumerate(input_str.read_text().strip().splitlines()):
    print(line)
    for c, ch in enumerate(line.strip()):
        if ch == "^":
            guard.add((r,c))
        elif ch == "#":
            obstacle.add((r,c))

guard_position = Point(*list(guard)[0]) # * unpacks the set object which is a tuple, because we need to move by modifying indexes
# we will store visited places in a different set

visited_location = set()
visited_location.add((guard_position.x, guard_position.y))
direction = "up"
while(0 <= guard_position.x < len(line) and 0<= guard_position.y < len(line)): # check if coordinates are inside of the length of the drawn map
    next_position = DIRECTION[direction](guard_position)
    #if next pos is an obstacle, turn right
    if (next_position.x, next_position.y) in obstacle:
        direction = TURN_RIGHT[direction]
    #else keep ER GOIN & add that location to a set (because sets cannot contain duplicate values)
    else:
        guard_position = next_position
        visited_location.add((guard_position.x, guard_position.y))

print("nr of unique visited locations: ", len(visited_location)-1)
#print("nr of unique visited locations: ", visited_location)



#print("positions of obstacles: ", obstacle) 

#  ....#.....
#  .........#
#  ..........
#  ..#.......
#  .......#..
#  ..........
#  .#..^.....
#  ........#.
#  #.........
#  ......#...


    

    










