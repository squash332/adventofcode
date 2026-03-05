import opcode2 as op
from opcode2 import arr

queues = [[]for _ in range(50)]
for i,q in enumerate(queues):
    q.append(i)

# print(queues)

computers = [op.IntCode(arr, queues[i]) for i in range(50)]

packets = [[] for _ in range(50)]
nat = None
last_nat_y = None

while True:
    idle = True
    if any(queues):
        idle = False
    
    for i,computer in enumerate(computers):
        incoming = computer.run()
        if incoming is not None:
            idle = False
            packets[i].append(incoming)

        # if queues
        if len(packets[i]) == 3:
            dest, x, y = packets[i]
            # print(f"dest:{dest}, x:{x}, y:{y}, queues:{queues}")

            if dest == 255:
                if nat is None:
                # print(f"dest:{dest}, nat:{nat[0]}")
                    print("part 1:", y)
                nat = (x, y)
                # exit()
            # print(packets[i])

            else:
                queues[dest].append(x)
                queues[dest].append(y)
                idle = False

            packets[i] = []
            # print(queues)
            # sleep(5)
    if all(len(q) == 0 for q in queues) and idle and nat:
        # write to address 0 
        x, y = nat
        # ("printing last packet", x, y)

        queues[0].append(x)
        queues[0].append(y)

        if y == last_nat_y:
            print("part 2:", y)
            break

        last_nat_y = y
            
        