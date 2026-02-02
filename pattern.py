# every towel marked with a pattern of colored stripes
# white w
# blue u
# black b
# red r
# green g

######### AVAILABLE TOWEL PATTERNS ##############
# r, wr, b, g, bwu, rb, gb, br 


######### LIST OF DESIRED DESIGNS ##############
# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb

# 6 out of 8 possible

from functools import lru_cache
from pathlib import Path

input_str = Path(__file__).parent / "towels.txt"

data = input_str.read_text().strip().splitlines()

#print(data)

new_patterns = []
empty = ''
patterns = data[0:1]
#print("given patterns: ", patterns, type(patterns))
#print("length of patterns list: ",len(patterns))
for line in patterns:
    for word in line.split(', '):
        new_patterns.append(word)

#print("novi patterns: ", new_patterns)

designs = data[2:]
#print("wanted designs: ", designs)
#print("blaa", len(designs))
possible_designs = 0 # nr of possible designs



# assume 0 designs possible, 
# first check the patterns with the biggest length
# n je length of najduzeg clana iz patterns
@lru_cache(None)
def find_permutations(line, n, index):
    if index == len(line):
        return 1
    
    #for value in patterns:
    total = 0

    for pattern in new_patterns:
        if line.startswith(pattern, index):
            total += find_permutations(line, n, index + len(pattern))
    # part_of_design = line[index:n] #trenutno 0:2
    
    return total
    #while sliced_string in designs:
        #
        #return find_permutations(line[i:], n-1, possible_designs)
        

    
    

num_designs = 0
n = len(max(new_patterns, key = len))
for line in designs:
    #print("** pozivanje **")
    #print(line)
    sum = find_permutations(line, n, 0)
    #print(sum)
    num_designs += sum


print(f"{num_designs} out of {len(designs)} design patterns are possible.")
        