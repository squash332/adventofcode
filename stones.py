# 7568 155731 0 972 1 6919238 80646 22 MY INPUT */
# blink == function call
# starts from the first index, goes up to the length
# 1 iteration = blink = initial size of array

# if number == 0, replace it with 1

# 0 1 10 99 999


   # The first stone, 0, becomes a stone marked 1.
   # The second stone, 1, is multiplied by 2024 to become 2024.
   # The third stone, 10, is split into a stone marked 1 followed by a stone marked 0.
   # The fourth stone, 99, is split into two stones marked 9.
   # The fifth stone, 999, is replaced by a stone marked 2021976.


   # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
   # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
   # The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
   # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)

   # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.


# So, after blinking once, your five stones would become an arrangement of seven stones engraved with the numbers 1 2024 1 0 9 9 2021976.
import math
from time import time

stones = [7568,155731, 0, 972, 1, 6919238, 80646, 22]

def blink(stones):
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = stones[i] + 1
            i += 1

        digit_count = len(str(stones[i]))
        #digit_count = print("digit count: ", digit_count)
        if digit_count % 2 == 0:
            exponent = int(digit_count / 2)
            #print(exponent) = 1
            #print(stones[i])
            second_digit = int(stones[i] % math.pow(10, exponent))
            #print(second_digit)
            stones.insert(i + 1, second_digit)
            stones[i] = int(stones[i] / math.trunc(math.pow(10, digit_count/2)))
            #print(stones)
            #print(digit_count) 2
            i += 2
        else :
            stones[i] *= 2024
            i += 1

print(stones)
j = 0
while j < 40:
    pre = time()
    blink(stones)
    after = time()
    in_ms = int((after - pre) * 1000)
    print(f"{j}: {in_ms}, num stones: {len(stones)}")
    # print("After ", j, "blinks", stones)
    j+=1
    



