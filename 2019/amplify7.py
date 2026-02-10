# each amplifier (A, B, C, D, E) needs to run a copy of program

# ask for phase setting (integer from 0 to 4), each is used ONCE - input instruction
# ask for amplifier's input signal - input instruction
# compute output signal, supply it back to amplifier with an output instruction

# if amplifier has not received input signal, wait until one arrives

# first amplifier's input value is 0, last amplifier output leads to thrusters

import opcode2 as op
from opcode2 import arr
from itertools import permutations

highest = 0


def run_phase(phase):
    output = 0
    for num in phase:
        outputs = op.run_loop(arr, inputs=[num, output])
        # print(f"output: {output}, num: {num}, outputs: {outputs}")
        output = outputs[-1]
    return output

highest = max(run_phase(phase)
              for phase in permutations([0, 1, 2, 3, 4]))

print(highest)
    




