import opcode2 as op
from opcode2 import arr
from collections import defaultdict

P = defaultdict(int)

def play():
    row = sorted([r for r,c in P])
    col = sorted([c for r,c in P])

    for r in range(row[0], row[-1]+1):
        for c in range(col[0], col[-1]+1):
            print(P[(r,c)], end='')
        print()
    return

computer = op.IntCode(arr, [2])
counter = 0

while True:
    computer.run()
    # print("comp result 1", computer.result)
    # print("comp result 1", computer.result[0])
    a = computer.result.pop(0)

    computer.run()
    # print("comp result 2", computer.result[0])
    b = computer.result.pop(0)

    computer.run()
    # print("comp result 3", computer.result)
    # print("comp result 3", computer.result[0])
    c = computer.result.pop(0)
    
    P[(b,a)] = c
    # print(a,b,c)
    if c== 2:
        counter += 1

    if computer.run():
        break

play()
# for k,v in P.items():
#         print(k,v)

# print("part 1:", counter)