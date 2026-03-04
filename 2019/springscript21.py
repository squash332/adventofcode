import opcode2 as op
from opcode2 import arr
# it can only remember 15 springscript instructions
# droid moves forward automatically, constantly thinking whether to jump
# springscript program defines logic for this decision, (overloading?)

# 4 spaces ahead
# A B C D E F G H I
# 1 2 3 4 5 6 7 8 9
springscript = ( # t, j false
"NOT A J\n" # if hole 1 tile ahead, prepare to jmp
"NOT B T\n" # 
"OR T J\n"  # if hole 2 steps ahead, consider jmp
"NOT C T\n" #
"OR T J\n"  # if hole three steps ahead, consider jmp
"AND D J\n" # only jmp if landing is ground
"NOT E T\n" # e hole?
"NOT T T\n" # t now true if E is ground
"OR H T\n"  # T true if E ground or H ground
"AND T J\n" # jump if landing on D doesnt kill me
"RUN\n")    # J true if any of a,b,c is hole and D is ground

input_queue = list("".join(springscript))
def input_func():
    return ord(input_queue.pop(0))

computer = op.IntCode(arr, input_func)

text = []
while True:

    output = computer.run()
    if output == None:
        break
    if output < 128:
        print(chr(output), end="")
    else:
        print("hull dmg:", output)


# 2 registers:
#   1) T - temporary value
#   2) J - jump register

# if jump register is true at the end of program, droid will try to jump
# both registers start as FALSE values



