import opcode2 as op
from opcode2 import arr
from collections import defaultdict

P = defaultdict(int)

def play():
    row = sorted([r for r,c in P])
    col = sorted([c for r,c in P])

    for k,v in P.items():
        if v == 3:
            paddle = k
        if v == 4:
            ball = k
    
    # for r in range(row[0], row[-1]+1):
    #     for c in range(col[0], col[-1]+1):
    #         match P[(r,c)]:
    #             case 0:
    #                 print(" ", end='')
    #             case 1:
    #                 print("|", end='')
    #             case 2:
    #                 print("#", end='')
    #             case 3:
    #                 print("_", end='')
    #             case 4:
    #                 print("o", end='')
        # print()
    
    if ball[1] < paddle[1]:
        return -1
    elif ball[1] > paddle[1]:
        return 1
    else:
        return 0

computer = op.IntCode(arr, play)
counter = 0
computer.memory[0] = 2
previous_score = None

while True:
    computer.run()
    if computer.result:
        a = computer.result.pop(0)

    computer.run()
    if computer.result:
        b = computer.result.pop(0)

    computer.run()
    if computer.result:
        c = computer.result.pop(0)
    
    P[(b,a)] = c
    if c== 2:
        counter += 1
    if a == -1 and b == 0 :
        current_score= c

        if current_score == previous_score:
            print("Final score", current_score)
            break
        previous_score = current_score
# print("part 1:", counter)