# one wire per line of text

from dataclasses import dataclass
import math
from pathlib import Path


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)
    
    def __mul__(self, num):
        return Point(self.x * num, self.y * num)


# def split_lists(list):
#     half = math.floor(len(list)) // 2
#     return list[:half], list[half:]


DIRECTIONS = {"U": Point(-1, 0), "R": Point(0, 1), "D": Point(1, 0), "L": Point(0, -1)}

WIRE1_STEPS = {}
WIRE2_STEPS = {}

input_str = Path(__file__).parent / "wires.txt"
arr = input_str.read_text().strip().split()
# print("data:", arr)

wire_1 = arr[0].split(",")
wire_2 = arr[1].split(",")
print("wire1:", wire_1)
# print("wire2:", wire_2)



wire1_visited = set()
wire2_visited = set()
wire_pos = Point(0, 0)
# central_port = (0,0)

step = 0
for instruction in wire_1:
    i = 0
    # print(instruction)
    wire1_visited.add(wire_pos)

    direction = instruction[0][:1]  # R 
    steps = int(instruction[1:])       # 8
    while i < steps: # spremi sve pozicije izmedju (0,0) i (0, 8)
        position = wire_pos + DIRECTIONS[direction]
        step += 1
        # print("positions in between 2 points to be added:", position)
        wire1_visited.add(position)
        if position not in WIRE1_STEPS:
            WIRE1_STEPS[position] = step
        wire_pos = position
        i += 1
    # print(f"wire1 positions after moving {instruction}: {wire_pos}")


step = 0       
wire_pos = Point(0, 0)
for instruction in wire_2:
    i = 0
    # print(instruction)
    wire2_visited.add(wire_pos)

    direction = instruction[0][:1]  # U
    steps = int(instruction[1:]) 
    while i < steps: # spremi sve pozicije izmedju (0,0) i (-7, 0)   
        position = wire_pos + DIRECTIONS[direction]
        step += 1
        # print("positions in between 2 points to be added:", position)
        wire2_visited.add(position)
        if position not in WIRE2_STEPS:
            WIRE2_STEPS[position] = step
        wire_pos = position
        i += 1

intersection = wire1_visited & wire2_visited
intersection.discard(Point(0,0))

#print(wire1_visited)

print("intersection: ", intersection)

smallest_total = None
for point in intersection:
    total = WIRE1_STEPS[point] + WIRE2_STEPS[point]
    #print("total", total)
    if smallest_total is None or total < smallest_total:
        smallest_total = total

print(smallest_total)
# steps1 = WIRE1_STEPS[]



# distances = []
# for point in intersection:
#     distances.append(abs(point.x) + abs(point.y))
    
# print("manhattan distance to closest:", min(distances))





        


# ...........
# .+-----+...
# .|.....|...
# .|..+--X-+.
# .|..|..|.|.
# .|.-X--+.|.
# .|..|....|.
# .|.......|.
# .o-------+.
# ...........
