import copy

import opcode2 as op
from opcode2 import arr
from dataclasses import dataclass
import ctypes
from random import choice
from collections import deque

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)
    
class MovementFunction:
    def __init__(self):
        self.last_direction = 1

    def __call__(self):
        return self.last_direction
def bfs():
    computer = op.IntCode(arr, MovementFunction())
    position = Point(0,0)
    queue = deque([(position, computer, 0)])
    visited = {}
    while queue:
        position, computer_state, dist = queue.popleft()
        # print(position)

        for direction in [1,2,3,4]:
            next_position = position + DIRECTIONS[direction]
            new_computer = computer_state.clone(MovementFunction())
            new_computer.inputs.last_direction = direction
            robot_answer = new_computer.run()

            if robot_answer == WALL:
                continue
            # print(position, computer_state, robot_answer)
            if next_position in visited:
                continue
            
            # print("woo", new_computer.inputs.last_direction)
            new_dist = dist + 1
            # print(new_dist)
            visited[next_position] = new_dist

            if robot_answer == OXYGEN:
                oxygen_position = next_position
                print("part 1:", new_dist) # previously, the return was here and that made BFS stop and not explore the whole "map"
                                           # our exit from the while loop is now the end of BFS (if correclty implemented -> queue always ends empty)
                
        
            # print(visited)
            # print(computer.memory)
            queue.append((next_position, new_computer, new_dist))
    return oxygen_position, visited


def oxygen_fill_time():
    oxygen_position, visited = bfs()
    max_time = 0
    # print(visited)
    # print(distance, oxygen_position)
    queue = deque ([(oxygen_position, 0)])
    seen = {oxygen_position}
    # print(queue)
    while queue:
        position, length = queue.popleft()
        max_time = max(max_time, length) 

        for direction in [1,2,3,4]:
            next_position = position + DIRECTIONS[direction]

            if next_position in visited and next_position not in seen:
                seen.add(next_position)
                queue.append((next_position, length +1 ))
        # print(queue)
    print("part 2:", max_time)
    return max_time  





DIRECTIONS = {
    1: Point(0, 1),   # north
    2: Point(0, -1),  # south
    3: Point(-1, 0),  # west
    4: Point(1, 0)    # east
    }
WALL, MOVED, OXYGEN = 0, 1, 2


oxygen_fill_time()



