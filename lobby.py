#
#
# https://adventofcode.com/2025/day/3

# example input:   largest possible joltage:
# 987654321111111   98   
# 811111111111119   89
# 234234234234278   78  
# 818181911112111   92

# total output joltage : 98 + 89 + 78 + 92 = 357

# find maximum joltage possible from each bank 

# search whole row -> find largest_num remember its index
# search whole row staring from largest_num -> find 2nd_largest_num
# add largest_num and 2nd_largest_num

#search next row

#repeat

from pathlib import Path

# print(0, "0", ord("0"))

input_str = Path(__file__).parent / "example.txt"
data = input_str.read_text().strip().splitlines()

def find_joltage(line, n, joltage=""):
    if n == 0:
        return int(joltage)
    my_max = max(line[:len(line)-n+1])
    i = line.index(my_max)

    joltage += my_max
    #print(f"{line}, {my_max=}, {joltage=}, {n=}, {i=}")
    # n = 2
    #print("blaaaaaaaaaaaaa" , line[i+1])
    return find_joltage(line[i+1:], n-1, joltage)
        
# for line in data

max_joltage = 0
for i,r in enumerate(data):
    joltage = find_joltage(r, 12)
    #print(f"{joltage=}")
    max_joltage += joltage
print("max joltage is: ", max_joltage)


# for line in data:
#     r = 1
#     m = ""
#     print("\nthis is the line", line)

#     my_max = max(line[0:-r])
#     i = line.index(my_max)
#     print("my index after first max", i)
#     print(line, "1st max num: ", my_max)
#     m += my_max

#     r = 0
#     my_max = max(line[i+1:-r], default=line[-1])
#     i = line.index(my_max)
#     print(line, "2nd max num: ", my_max)
#     m += my_max
#     print("highest possible jolt: ", m)




# for i, c in enumerate(line):
#     print(i, c)

# r = 1
# my_max = max(line[i+1:-r]) # 6: -(-1)
# i = line.index(my_max)
# print(line, "max num ", my_max, "type of my_max: ", type(my_max))
# m += my_max



# with open("example.txt") as banks:
#         sum = 0
#         for line in banks:
#             line = list(line.strip())
#             print(type(line))
#             start = 0 # start of input
#             end = len(line) - 1  #end of input
#             #print(end)
            
        
                    
        
                    
              




