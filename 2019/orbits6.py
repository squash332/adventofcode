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
        total_orbits += each_planet_orbit(planet, DIRECT_ORBITS)
    print("total orbits:", total_orbits)

def distances_from(start, direct_orbits):
    distance = {}
    steps = 0
    current = start

    while current in direct_orbits:
            distance[current] = steps
            current = direct_orbits[current]
            steps += 1
    return distance

def count_p2_orbits(me, santa, direct_orbits):
    distance_from_me  = distances_from(me, direct_orbits)
    current = santa
    orbits = 0

    while current not in distance_from_me:
        current = direct_orbits[current]
        orbits += 1
    return orbits + distance_from_me[current]

total_orbit_count(orbits)
count_for_planets()
me = DIRECT_ORBITS["YOU"]  
santa = DIRECT_ORBITS["SAN"] 
print(me, santa)

p2_orbits = count_p2_orbits(me, santa, DIRECT_ORBITS)


print(f"p2 orbits: {p2_orbits}")





