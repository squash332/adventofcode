from collections import defaultdict
from copy import deepcopy
from pathlib import Path

input_str = Path(__file__).parent / "intcode.txt"
memory = input_str.read_text().strip().splitlines()
arr = []

for line in memory:
    for word in line.split(','):
        arr.append(word)

arr = list(map(int, arr))
class IntCode:

    def __init__(self, memory, inputs, i=0, mode=0,result=None):
        self.memory = memory
        self.i = i
        self.mode = 0
        self.inputs = inputs 
        self.result = None
        self.relative_base = 0
        self.extended = []
        self.halted = False

    def run(self):
        while True:
            opcode, mode = self.decode()
            self.mode = mode
            if opcode == 99:
                self.halted = True
                return None
            
            self.i = OPCODES[opcode](self)

            if opcode == 4 :
                return self.result
    
    def add(self):
        a = self.read_param(1)
        b = self.read_param(2)
        self.memory[self.write_addr(3)] = a + b
        return self.i + 4
        

    def multiply(self):
        a = self.read_param(1)
        b = self.read_param(2)
        self.memory[self.write_addr(3)] = a * b
        return self.i + 4
        
    def input(self):
        inputs = self.inputs()
        self.memory[self.write_addr(1)] = inputs
        return self.i + 2
        
    def output(self):
        self.result = self.read_param(1)
        return self.i + 2

    def decode(self):
        decoded_opcode = self.memory[self.i] % 100
        mode = self.memory[self.i] // 100

        return decoded_opcode, mode 

    def get_mode(self, param_index): 
        return self.mode // (10 ** param_index) % 10
         

    def read_param(self, offset):
        # print("printing offset:", offset)
        param_mode = self.get_mode(offset - 1)
        value = self.memory[self.i + offset]
        # print(f"param_mode {param_mode}, offset {offset}, value {value}, self.i {self.i} ")

        if param_mode == 1: # parameter interpreted as value aka mode 1 POSITION MODE
            return value
        elif param_mode == 2: # relative mode
            # print("printing the return from param_mode 2:", self.memory[self.relative_base])
            return self.memory[self.relative_base + value]
        else:
            self.memory += ([0] * value)
            return self.memory[value] # IMMEDIATE VALUE

    def write_addr(self, offset):
        param_mode = self.get_mode(offset - 1)
        value = self.memory[self.i + offset]
        if param_mode == 0: #pos
            # print(f" param mode 0 value: {value}")
            self.memory += ([0] * value)
            return value
        elif param_mode == 2: #rel
            # print(f"elif self.rel_base: {self.relative_base}")
            # print(f"elif value : {value}")
            return self.relative_base + value


    def jump_true(self):
        first = self.read_param(1)
        second = self.read_param(2)
        if first != 0:
            self.i = second
            return self.i
        else:
            return self.i + 3

    def jump_false(self):
        first = self.read_param(1)
        second = self.read_param(2)
        if first == 0:
            self.i = second
            return self.i
        else:
            return self.i + 3

    def less_than(self):
        first = self.read_param(1)
        second = self.read_param(2)
        if first < second:
            self.memory[self.write_addr(3)] = 1
        else:
            self.memory[self.write_addr(3)]= 0
        return self.i + 4

    def equals(self):
        first = self.read_param(1)
        second = self.read_param(2)
        if first == second:
            self.memory[self.write_addr(3)]= 1
        else:
            self.memory[self.write_addr(3)] = 0
        return self.i + 4
    
    def relative_base_offset(self):
        first = self.read_param(1)
        self.relative_base += first
        # print(f"relative base: {self.relative_base}")

        return self.i + 2


OPCODES = {
    1: IntCode.add,
    2: IntCode.multiply,
    3: IntCode.input,
    4: IntCode.output,
    5: IntCode.jump_true,
    6: IntCode.jump_false,
    7: IntCode.less_than,
    8: IntCode.equals,
    9: IntCode.relative_base_offset
}

def run_program(arr, inputs):

    intcode = IntCode(deepcopy(arr), 0, 0, inputs, [])
    while True: 
        opcode, mode = intcode.decode()
        intcode.mode = mode
        if opcode == 99:
            break
        intcode.i = OPCODES[opcode](intcode)

    return intcode.result

# print(run_program(arr, []))



