from collections import defaultdict
from dataclasses import dataclass
from dataclasses import astuple
from itertools import count

import opcode2 as op
from opcode2 import arr

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    
    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

def output(pos):

    scaffolds = set ()
    robot_position= set () 
    
    grid = ''.join(chr(x) for x in pos )
    # print(grid)
    lines = grid.strip().split('\n')

    for r, row in enumerate(lines):
        for c, ch in enumerate(row):
            if ch == '#':
                scaffolds.add((r,c))
            if ch == "^":
                robot_position.add((r,c))

    return scaffolds, robot_position

def find_intersections(scaffolds):

    sum = 0
    for x in scaffolds:
        position = Point(*x)
        neighbours = []

        for direction in [1,2,3,4]:
            next_position = position + DIRECTIONS[direction]

            if (next_position.x, next_position.y) in scaffolds:
                neighbours.append(next_position)
            else:
                continue
        if len(neighbours) == 4:
            sum += position.x * position.y
    print("part 1:", sum)

def right(direction):
    return 1 if direction == 4 else direction + 1

def left(direction):
    return 4 if direction == 1 else direction - 1

def main_movement_routine(scaffolds, robot_position):

    position_tuple = next(iter(robot_position))
    position = Point(*position_tuple)
    current_direction = 1
    pathing = []
    while True:
        steps = 0
        while True:
            next_position = position + DIRECTIONS[current_direction] 
        
            if (next_position.x, next_position.y) in scaffolds:
                position = next_position
                steps += 1
            else:
                break
        if steps > 0:
            pathing.append(str(steps))

        left_dir = left(current_direction)
        right_dir = right(current_direction)

        left_pos = position + DIRECTIONS[left_dir]
        right_pos = position + DIRECTIONS[right_dir]

        if (left_pos.x, left_pos.y) in scaffolds:
            current_direction = left_dir
            # pathing.append(int(ord("L"))) # 76

            pathing.append("L")
        elif (right_pos.x, right_pos.y) in scaffolds:
            current_direction = right_dir
            # pathing.append(int(ord("R"))) # 82

            pathing.append("R")
        else:
            break
    # print("message", pathing)
    a = find_longest_prefix(pathing)
    replaced_a = replace_pathing(pathing, a, "A")
    # print("replaced A", replaced_a)

    b = find_longest_prefix(replaced_a)
    replaced_b = replace_pathing(replaced_a, b, "B")
    # print("replaced B:", replaced_b)

    c = find_longest_prefix(replaced_b)
    replaced_c = replace_pathing(replaced_b, c, "C")
    # print("replaced C:", replaced_c)
    # path_a, path_b, path_c = split_routine(pathing)
    return replaced_c, a, b, c

def find_longest_prefix(pathing, max_len=20):
    i = 0
    while i < len(pathing) and pathing[i] in {"A", "B", "C"}:
        i += 1
    # print("printing i:", i)
    best = None
    for end in range(i + 2,len(pathing) + 1,2):
        prefix = pathing[i:end]

        if any(token in {"A", "B", "C"} for token in prefix):
            break
        if len(",".join(prefix)) <= max_len:
            best = prefix
        else:
            break
    return best
    

def replace_pathing(sequence, match, character):
    result = []
    i =0

    while i < len(sequence):
        if sequence[i:i+len(match)] == match:
            result.append(character)
            # print("appended character to result")
            i += len(match)
        else :
            result.append(sequence[i])
            i += 1
    return result
        
def to_ascii_line(characters):
    return [ord(c) for c in ",".join(characters)] + [10]


computer = op.IntCode(arr, lambda:0)
computer.memory[0] = 2

DIRECTIONS = {
    1: Point(-1, 0),   # up
    2: Point(0, 1),  # right
    3: Point(1, 0),  # down
    4: Point(0, -1)  # left
    } 

pos = []
while True:

    element = computer.run()
    if element == None:
        break
    pos.append(element)

scaffolds, robot_position = output(pos)
find_intersections(scaffolds)
main_routine, A, B, C = main_movement_routine(scaffolds, robot_position)

# print("main routine:", main_routine, A, B, C)
length = len(main_routine)
ascii_routine = []

for i, ch in enumerate(main_routine):
    # print(i, ch)
    ascii_routine.append(ord(ch))
    if i < length - 1:
        ascii_routine.append(ord(","))
    else :
        ascii_routine.append(10)

# print(ascii_routine)

ascii_input = []
ascii_input += to_ascii_line(main_routine)
ascii_input += to_ascii_line(A)
ascii_input += to_ascii_line(B)
ascii_input += to_ascii_line(C)
ascii_input += [ord('n'), 10]

# print("ascii input:", ascii_input)

# print(ascii_routine)
computer = op.IntCode(arr, lambda: ascii_input.pop(0))
computer.memory[0] = 2

while True:
    
    result = computer.run()
    if result == None:
        break
    last_output = result

print("part 2:", last_output)