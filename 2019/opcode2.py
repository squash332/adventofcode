from copy import deepcopy
from pathlib import Path
input_str = Path(__file__).parent / "intcode.txt"
memory = input_str.read_text().strip().splitlines()
arr = []

for line in memory:
    for word in line.split(','):
        arr.append(word)

arr = list(map(int, arr))


# def get_wanted_output(my_output):
#     my_output += find_output(0, 0) # 337106
#     if my_output == wanted_output:
#         return my_output
# instruction e.g 1,2,3,4 -> 1 is opcode; 2, 3, 4 parameters
# 1002, 4, 3, 4, 33

def add(memory, i, mode, input, output):
    a = read_param(memory, i, 1, mode)
    b = read_param(memory, i, 2, mode)
    memory[write_addr(memory, i, 3)] = a + b
    return i + 4
    

def multiply(memory, i, mode, input, output):
    a = read_param(memory, i, 1, mode)
    b = read_param(memory, i, 2, mode)
    memory[write_addr(memory, i, 3)] = a * b
    return i + 4
    

def input(memory, i, mode, input, output):
    memory[write_addr(memory, i, 1)] = input
    return i + 2
    
def output(memory, i, mode, input, output_list):
    value = memory[read_param(memory, i, 1, 1)]
    output_list.append(value)
    return i + 2

def decode(memory, i):
    decoded_opcode = memory[i] % 100
    # if decoded_opcode not in OPCODES:
    #     decoded_opcode %= memory[i]
    mode = memory[i] // 100

    return decoded_opcode, mode # for 1002, opcode 2, mode 10

def get_mode(mode, param_index): #10
    return mode // (10 ** param_index) % 10

def read_param(memory, i, offset, mode):
    param_mode = get_mode(mode, offset - 1)
    value = memory[i + offset]

    if param_mode == 1: # parameter interpreted as value aka mode 1 POSITION MODE
        return value
    else:
        return memory[value] # IMMEDIATE VALUE

def write_addr(memory, i, offset):
    return memory[i + offset]

def jump_true(memory, i, mode, input, output):
    #e.g 1111, 11 opcode (1) -> non zero, params 11 -> sets instruction pointer to 11
    first = read_param(memory, i, 1, mode)
    second = read_param(memory, i, 2, mode)
    if first != 0:
        i = second
        return i
    else:
        return i + 3

def jump_false(memory, i, mode, input, output):
    first = read_param(memory, i, 1, mode)
    second = read_param(memory, i, 2, mode)
    if first == 0:
        i = second
        return i
    else:
        return i + 3

def less_than(memory, i, mode, input, output):
    first = read_param(memory, i, 1, mode)
    second = read_param(memory, i, 2, mode)
    if first < second:
        memory[write_addr(memory, i, 3)] = 1
    else:
        memory[write_addr(memory, i, 3)]= 0
    return i + 4

def equals(memory, i, mode, input, output):
    first = read_param(memory, i, 1, mode)
    second = read_param(memory, i, 2, mode)
    if first == second:
        memory[write_addr(memory, i, 3)]= 1
    else:
        memory[write_addr(memory, i, 3)] = 0
    return i + 4


OPCODES = {
    1: add,
    2: multiply,
    3: input,
    4: output,
    5: jump_true,
    6: jump_false,
    7: less_than,
    8: equals
}

def run_loop(arr, input_instruction):
    memory = deepcopy(arr)
    i = 0
    result = []
    while True: 
        opcode, mode = decode(memory, i)
        # print("opcode", opcode, type(mode))
        # print("mode", mode, type(mode))
        # print("getmode:", get_mode(mode, ))
        if opcode == 99:
            break
        print(f"i={i}, instr={memory[i]}, opcode={opcode}, mode={mode}")
        i = OPCODES[opcode](memory, i, mode, input_instruction, result)

    return result

print(run_loop(arr, 5))

# print("Part 1:", find_output(12,2))


# wanted_output = 19690720
# for noun in range(100):
#     for verb in range(100):
#         if find_output(noun, verb) == wanted_output:
#             answer = 100 * noun + verb
#             print(f"Part 2: {answer}")
#             exit()


    # arr[1] = noun
    # arr[2] = verb
    # for i, number in enumerate(arr):
    #     #print(i, number)
    #     result = 0
    #     if number == 99 and i % 4 == 0:
    #         break
    #     elif number == 1 and i % 4 == 0:
    #         add(i) 
    #     elif number == 2 and i % 4 == 0 :
    #         multiply(i)  
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

