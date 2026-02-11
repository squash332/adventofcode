import math
from pathlib import Path
from collections import Counter

input_str = Path(__file__).parent / "input.txt"
data = input_str.read_text().strip().splitlines()



IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6
SPLIT = IMAGE_WIDTH * IMAGE_HEIGHT # 6

string = data[0]

images = dict ()

val = "0"
index = 0
zeros = {}
for i in range(0, len(string), SPLIT): # start 0 end 12 step 6
    sum = 0
    layer = string[i:i+SPLIT]
    row = 0 
    while row < IMAGE_HEIGHT:
        start = row * IMAGE_WIDTH 
        end = start + IMAGE_WIDTH

        images[index] = layer[start:end]
        for numbers in images[index]:
            if val == numbers:
                sum += 1
                zeros[layer] = sum
        row += 1
        index += 1

min_zeros = min(zeros.values())

for k, v in zeros.items():
    if v == min_zeros:
        wanted_number = k

wanted_list = Counter(wanted_number)

for k in wanted_list.keys():
    if k == '2':
        first = int(wanted_list[k])
    elif k == '1':
        second = int(wanted_list[k])

print(first*second)




 






    
