# map indicates if position empty
# EMPTY -> .
# ASTEROID -> #

from collections import defaultdict
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

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

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


highest = 0
result = {}
for i, asteroid in enumerate(asteroids):
    result[asteroid] = find_best_planet(asteroid, asteroids)

station = max(result, key=result.get)
print(station)
best_value = max(result.values())
print(f" ({station.y},{station.x}) detected asteroids: {best_value}")

angles = defaultdict(list)
for asteroid in asteroids:
    if asteroid == station:
        continue

    x = asteroid.x - station.x
    y = asteroid.y - station.y

    angle = math.atan2(y, -x) # found up direction
    if angle < 0:
        angle += 2 * math.pi

    distance = math.sqrt(x*x + y*y)
    angles[angle].append((distance, asteroid))
    # print(angle)
    # print(f"asteroid {asteroid}, new: ({x},{y})")

for angle in angles:
    angles[angle].sort()

clockwise = sorted(angles.keys())
# print(angles)


count = 0
while True:
    for angle in clockwise:
        if angles[angle]:
            distance, asteroid = angles[angle].pop(0)
            # print(distance, asteroid)
            count += 1

            if count == 200:
                print(f"{(asteroid.y,asteroid.x)} -> X*100 + Y = {asteroid.y}*100+{asteroid.x} = {asteroid.y*100 + asteroid.x}")
                exit()











