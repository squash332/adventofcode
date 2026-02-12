# each amplifier (A, B, C, D, E) needs to run a copy of program

# ask for phase setting (integer from 0 to 4), each is used ONCE - input instruction
# ask for amplifier's input signal - input instruction
# compute output signal, supply it back to amplifier with an output instruction

# if amplifier has not received input signal, wait until one arrives

# first amplifier's input value is 0, last amplifier output leads to thrusters

from copy import deepcopy
import opcode2 as op
from opcode2 import arr
from itertools import permutations

class Amplifier():
    def __init__(self, program, phase):
        self.memory = deepcopy(program)
        self.i = 0
        self.inputs = [phase]
        self.halted = False
    
    def __call__(self, signal):
        self.inputs.append(signal)

        output_list = []
        while True:
            opcode, mode = op.decode(self.memory, self.i)

            if opcode == 99:
                self.halted = True  
                return None

            if opcode == 3 and not self.inputs:
                return 
            
            self.i = op.OPCODES[opcode](self.memory, self.i, mode, self.inputs, output_list)
            
            if opcode == 4:
                return output_list[-1]

def feedback_loop(program, phase):
    amps = [Amplifier(program, p) for p in phase] 
    signal = 0
    while not amps[-1].halted:
        for amp in amps:
            value = amp(signal)
            # print("printing value", value)
            if value is not None:
                signal = value
                # print("printing signal", signal)
    
    return signal
        
    
def run_phase(phase):
    output = 0
    for num in phase:
        outputs = op.run_loop(arr, inputs=[num, output])
        # print(f"output: {output}, num: {num}, outputs: {outputs}")
        output = outputs[-1]
    return output

highest = max(feedback_loop(arr, phase)
            for phase in permutations(range(5,10)))

print(highest)




