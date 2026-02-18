import opcode2 as op
from opcode2 import arr

computer = op.IntCode(arr)
counter = 0
while True:
    computer.run()
    computer.result.pop(0)
    computer.run()
    computer.result.pop(0)
    computer.run()

    block_id = computer.result.pop(0)
    if block_id == 2:
        counter += 1

    if computer.run():
        break
print("printing results:", counter)