# map indicates if position empty
# EMPTY -> .
# ASTEROID -> #

import math
from pathlib import Path
from dataclasses import astuple, dataclass, fields

input_str = Path(__file__).parent / "input.txt"
data = input_str.read_text().strip().splitlines()

print(data)

@dataclass(frozen=True)
class Point:
    x: int
    y: int

asteroids = set ()

for r, line in enumerate(data):
    for c, ch in enumerate(line.strip()):
        if ch == "#":
            asteroids.add(Point(r, c))


def find_best_planet(asteroid, asteroids):
    counter = set ()

    for other in asteroids:
        if other == asteroid:
            continue
        x = other.x - asteroid.x
        y = other.y - asteroid.y
        gcd = math.gcd(x,y)
        x //= gcd
        y //= gcd
        # if asteroid == Point(3,4):
        #     print(f"asteroid: {asteroid}, other: {other}, x: {x}, y: {y}, gcd: {gcd} ")
        counter.add((x,y))
    return len(counter)

highest = 0

for asteroid in asteroids:
    result = find_best_planet(asteroid, asteroids)
    # print("result: ", result)
    highest = max(highest, result)

print(highest)


# print(counter)     
        

    
        


    # print(f"asteroid: {selected} location with {} ")








