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
DIRECT_ORBITS = {}

COM = 'COM'

def total_orbit_count(orbits):
    for i, orbit in enumerate(orbits): 
            # print(i, orbit, "len(orbits[i]):", len(orbits[i]))
            if COM in orbit:
                #   print("printing COM constant:", COM)
                  first = COM
                  second = orbit[len(first)+1:]
            else:
                first = orbit[:(len(orbits[i]) - 1) // 2]
                second = orbit[((len(orbits[i]) - 1) // 2)+1:]

            DIRECT_ORBITS[second] = first 

    # print("direct orbits:", DIRECT_ORBITS)

def each_planet_orbit(planet, direct_orbits):
    count = 0
    while planet in direct_orbits:
        #   print(f"count_orbits func: planet: {planet}, direct_orbits: {direct_orbits}")
          planet = direct_orbits[planet]
          count += 1
    return count

def count_for_planets():
    total_orbits = 0
    for planet in DIRECT_ORBITS:
        # print("planet:", planet)
        total_orbits += each_planet_orbit(planet, DIRECT_ORBITS)
    print("total orbits:", total_orbits)
# direct orbits is simply length of input
# DFS
total_orbit_count(orbits)
count_for_planets()                 


