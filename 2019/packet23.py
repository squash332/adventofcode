import opcode2 as op
from opcode2 import arr

queues = [[]for _ in range(50)]
for i,q in enumerate(queues):
    q.append(i)

print(queues)

computers = [op.IntCode(arr, queues[i]) for i in range(50)]

packets = [[] for _ in range(50)]
while True:
    for i,computer in enumerate(computers):

        incoming = computer.run()
        if incoming is not None:
            packets[i].append(incoming)


        if len(packets[i]) == 3:
            dest, x, y = packets[i]
            
            if dest == 255:
                print("part 1:", y)
                exit()
            # print(packets[i])

            queues[dest].append(x)
            queues[dest].append(y)

            packets[i] = []
            # print(queues)
        
            
        