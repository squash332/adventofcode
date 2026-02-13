import math
from pathlib import Path
from collections import Counter


input_str = Path(__file__).parent / "input.txt"
data = input_str.read_text().strip().splitlines()


IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6
SPLIT = IMAGE_WIDTH * IMAGE_HEIGHT 
print(len(data[0]) // SPLIT) # NR OF LAYERS 

string = data[0]

val = "0"
index = 0
print(string)
layers = []

for i in range(0,len(string),SPLIT):
    layers.append(string[i:i+SPLIT])



final = list([ "2" ] * SPLIT )
print("FINAL+++++++++++++++++++", final)

for i in range(len(layers)-1,-1,-1):
    for j in range(len(layers[i])):
        if layers[i][j] in (["0", "1"]):
            final[j] = layers[i][j]


for i in range(0, SPLIT, IMAGE_WIDTH):
    print("".join(final[i:i+IMAGE_WIDTH]).replace("0", " ").replace("1", "X"))


        


            

# 0 is black
# 1 is white
# 2 is transparent


 






    
