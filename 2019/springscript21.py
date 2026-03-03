import opcode2 as op
from opcode2 import arr
# it can only remember 15 springscript instructions
# droid moves forward automatically, constantly thinking whether to jump
# springscript program defines logic for this decision, (overloading?)

# 4 spaces ahead
# A B C D E F G H I
# 1 2 3 4 5 6 7 8 9
springscript = ( # t, j false
"NOT A J\n" # 
"NOT B T\n" # j je true 2 mjesto ispred pod
"OR T J\n"
"NOT C T\n"
"OR T J\n"
"AND D J\n"
"RUN\n")

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



