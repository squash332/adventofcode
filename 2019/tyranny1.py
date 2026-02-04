import math
from pathlib import Path

input_str = Path(__file__).parent / "input.txt"
masses = input_str.read_text().strip().splitlines()

fuel = 0
total = 0
for mass in masses:
    fuel = math.floor(int(mass) / 3) - 2
    sum = 0
    while fuel > 0:
        sum += fuel
        fuel = math.floor(fuel / 3) - 2
    # print(sum)
    total += sum

print(total)