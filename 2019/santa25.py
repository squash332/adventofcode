import opcode2 as op
from opcode2 import arr
from itertools import combinations


def to_ascii_line(characters):
    return [ord(c) for c in characters] + [10]

def find_secret_weight():
    combs = []
    for r in range(len(inventory) + 1):
        for item in combinations(inventory, r):
            combs.append(item)
        
    return combs
            
def drop_items():
    for item in inventory[:]:
        computer.inputs.extend(to_ascii_line("drop " + item))
        inventory.remove(item)

def try_combinations():
    all_combs = find_secret_weight()

    for comb in all_combs:
        drop_items()

        for item in comb:
            computer.inputs.extend(to_ascii_line("take " + item))
            inventory.append(item)
        computer.inputs.extend(to_ascii_line("west"))

    

inventory = []
command = ""
commands = ['north', 'take dark matter', 'north', 'north', 'take manifold', 'west', 'take jam', 'east', 'east', 'take candy cane', 'north', 'south', 'west', 'west', 'east', 'south', 'east', 'west', 'east', 'south', 'take antenna', 'west', 'take hypercube', 'east', 'west', 'north', 'south', 'east', 'south', 'north', 'west', 'north', 'south', 'east', 'north', 'west', 'east', 'west', 'south', 'south', 'west', 'south', 'west', 'west', 'inv', 'east', 'north', 'east', 'north', 'east', 'esat', 'east', 'take bowl of rice', 'west', 'south', 'take dehydrated water', 'east', 'west', 'north', 'south', 'east', 'west', 'north', 'west', 'north', 'north', 'south', 'south', 'south', 'west', 'east', 'north', 'north', 'north', 'east', 'north', 'sotuh', 'south', 'west', 'west', 'east', 'south', 'south', 'west', 'south', 'west', 'south', 'west', 'west']
computer = op.IntCode(arr, command)

i = 0
while True:
    result = computer.run()
    if result is None:
        if i < len(commands):
            command = commands[i]
            i += 1
        else:
            try_combinations()
            # command = "west"
            # commands.append(command)
        computer.inputs.extend(to_ascii_line(command))
        if command.startswith('take '):
            item = command[5:]
            inventory.append(item)
        elif command.startswith('drop '):
            item = command[5:]
            inventory.remove(item)
        if command == 'exit':
            print(commands)
            break

        continue
    print(chr(result), end="")





