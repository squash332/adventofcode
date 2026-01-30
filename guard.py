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


from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from xml.etree.ElementTree import tostring


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def is_inside(self, dimensions: "Point") -> bool:
        return 0 <= self.x < dimensions.x and 0 <= self.y < dimensions.y


input_str = Path(__file__).parent / "pathing.txt"
arr = []

guard = Point(0,0)
obstacle = set()

data = input_str.read_text().strip().splitlines()

DIRECTIONS = [Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)]
DIMENSIONS = Point(len(data), len(data[0]))

for r, line in enumerate(data):
    for c, ch in enumerate(line.strip()):
        if ch == "^":
            guard = Point(r, c)
        elif ch == "#":
            obstacle.add(Point(r, c))

#print("dimensions: ", DIMENSIONS)

visited_location = set()
#print(guard)

def part_1(guard):
    current_direction = 0 # Set current direction as going up
    while True:  # check if coordinates are inside of the length of the drawn map
        next_position = guard + DIRECTIONS[current_direction]
        if not next_position.is_inside(DIMENSIONS):
            break

        elif next_position in obstacle:
            current_direction = (current_direction + 1) % len(DIRECTIONS)
        else:
            guard = next_position
            visited_location.add(guard)
    return visited_location




def part_2(guard):
    pathing = part_1(guard)
    n_loops = 0 
    
    for p in pathing:
        if p == guard:
            continue

        g = guard
        visited = set()
        with_added_obstacle = deepcopy(obstacle) # copying all obstacles
        
        #print("pathing : ", pathing, "\np: ",p )

        with_added_obstacle.add(p)
        
        current_direction = 0
        
        while True: 
            visited.add((g, current_direction))
            next_position = g + DIRECTIONS[current_direction] 

            if (next_position, current_direction) in visited:
                
                n_loops += 1
                break
            
            if not next_position.is_inside(DIMENSIONS):
                break

            if next_position in with_added_obstacle: 
                current_direction = (current_direction + 1) % len(DIRECTIONS) 
                

            else:
                g = next_position
    return n_loops

print(f"Number of loops possible {part_2(guard)}")




#  ..#...
#  .....#
#  ......
#  .#^...
#  ....#.

# cycle counter

# def print_map(visited, obstacles, guard):
#     for x in range(DIMENSIONS.x):
#         for y in range(DIMENSIONS.y):
#             p = Point(x,y)
#             if p == guard:
#                 print("*", end="")
#                 continue
#             elif p in obstacles:
#                 print("#", end="")
#                 continue

#             visited= False
#             for v,_ in visited_location:
#                 if p == v:
#                     print("@", end="")
#                     visited = True
#                     break

#             if not visited:
#                 print(".", end="")
#         print()
#     print("\n\n")

# #print("positions of obstacles: ", obstacle)