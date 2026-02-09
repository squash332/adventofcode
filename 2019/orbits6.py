from pathlib import Path
import re

input_str = Path(__file__).parent / "input.txt"
orbits = input_str.read_text().strip(')').splitlines()

# print(data)
# char=')'

# orbits = [orbit.replace(char, '') for orbit in data]

# no duplicates in sets
# 
# print(orbits)
PLANETS = set ()
DIRECT_ORBITS = {
    0: "COMB",

}
INDIRECT_ORBITS = set()

COM = 'COM'

def total_orbit_count(orbits):
    sum = 0
    current = ''
    for i, orbit in enumerate(orbits): 
            print(i, orbit)
            if COM in orbit:
                  print("printing COM constant:", COM)
                  first = COM
                  second = orbit[len(first)+1:]
            else:
                first = orbit[0:(len(orbits[i]) - 1) // 2]
                second = orbit[-((len(orbits[i]) - 1) // 2)]
            print(f"i: {i} first: {first}")
            print(f"u: {i} second: {second}")

            DIRECT_ORBITS[i] = first + second
            PLANETS.add(first)
            PLANETS.add(second) 

    sum += len(PLANETS)
    print(f"planets: {PLANETS},\norbit sum: {sum}")
    print("direct orbits:", DIRECT_ORBITS)


# direct orbits is simply length of input
        
total_orbit_count(orbits)                 


