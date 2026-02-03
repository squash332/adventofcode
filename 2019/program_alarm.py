from copy import deepcopy
from pathlib import Path
from functools import lru_cache
input_str = Path(__file__).parent / "intcode.txt"
data = input_str.read_text().strip().splitlines()
arr = []

for line in data:
    for word in line.split(','):
        arr.append(word)

arr = list(map(int, arr))

def opcode_add(data, i):
    data[data[i+3]] = data[data[i + 1]] + data[data[i + 2]]

def opcode_multiply(data, i):
    data[data[i+3]] = data[data[i + 1]] * data[data[i + 2]]

def get_wanted_output(noun, verb, my_output):
    my_output += find_output(0, 0) # 337106
    if my_output == wanted_output:
        return my_output
    
    
    

def find_output(noun, verb):
    data = deepcopy(arr)
    data[1] = noun
    data[2] = verb
    program_counter = 0
    while True:  
        opcode = data[program_counter]
        
        if opcode == 99:
            break

        if opcode == 1:
            opcode_add(data, program_counter)  

        if opcode == 2:
            opcode_multiply(data, program_counter)     

        program_counter += 4

    print("noun:", noun, "verb:", verb)
    return data[0]

print("Part 1:", find_output(12,2))


wanted_output = 19690720
for noun in range(100):
    for verb in range(100):
        if find_output(noun, verb) == wanted_output:
            answer = 100 * noun + verb
            print(f"Part 2: {answer}")
            exit()


    # arr[1] = noun
    # arr[2] = verb
    # for i, number in enumerate(arr):
    #     #print(i, number)
    #     result = 0
    #     if number == 99 and i % 4 == 0:
    #         break
    #     elif number == 1 and i % 4 == 0:
    #         opcode_add(i) 
    #     elif number == 2 and i % 4 == 0 :
    #         opcode_multiply(i)  
    # my_output = arr[0]
    # print("noun:", noun, "verb:", verb)   
    # return my_output

#print("the answer is:", get_wanted_output(12,2, find_output(12,2)))


#print(f"the output is: {find_output(12,2)}, with the noun {noun} and verb {verb}")
#print(f"answer for part 2 is {answer}")


# pt2 
# determine inputs that produce output 19690720
# inputs are provided by 




# 1,9,10,3,     1,9,10,70,
# 2,3,11,0,
# 99,
# 30,40,50
# EXAMPLE -> 1 represents (1, addition), 9 & 10 positions of inputs, 3 position of output
# (1, addition) arr[3] = arr[8] + arr[9]

# forward 4 steps -> (2, multiplication) arr[0] = arr[3] * arr[11]
# 

# opcode - value at position 0 which indicates what to do (1, 2 or 99) 
# 99 means program is finished and should halt
# encountering a different opcode means something went wrong

# if the opcode is 1, the next 2 positions add up and overwrite the number at 3rd position
# opcode 2 works exactly like 1, it just multiplies

# when done with an opcode, move forward 4 steps

