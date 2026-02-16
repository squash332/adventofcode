# map indicates if position empty
# EMPTY -> .
# ASTEROID -> #

import math
from pathlib import Path
from dataclasses import astuple, dataclass, fields

input_str = Path(__file__).parent / "input.txt"
data = input_str.read_text().strip().splitlines()

# print(data)

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
        counter.add((x,y))
    return len(counter)

def vaporize_asteroids():
    return

highest = 0
result = {}
for i, asteroid in enumerate(asteroids):
    result[asteroid] = find_best_planet(asteroid, asteroids)


best_asteroid = max(result, key=result.get)
best_value = max(result.values())
print(f" ({best_asteroid.y},{best_asteroid.x}), detected asteroids: {best_value}")








