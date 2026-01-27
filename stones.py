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
from collections import defaultdict
from functools import cache, reduce
import math
import operator
from time import time

# stones = [125, 17]
stones = [7568, 155731, 0, 972, 1, 6919238, 80646, 22]


# def blink(stones):
    
#     i = 0
#     while i < len(stones): # 0 < 1 ?
#         if stones[i] == 0:
#             stones[i] = stones[i] + 1
#             i += 1

#         digit_count = len(str(stones[i]))
#         if digit_count % 2 == 0:
#             exponent = int(digit_count / 2)
#             second_digit = int(stones[i] % math.pow(10, exponent))
#             stones.insert(i + 1, second_digit)
#             stones[i] = int(stones[i] / math.trunc(math.pow(10, digit_count/2)))
#             i += 2

#         else :
#             stones[i] *= 2024
#             i += 1
#     return stones

blinked = defaultdict(list)

@cache 
def blink_n(stone, n):
    if n == 0:
        return 1
    # blinked[n].append(stone)

    digit_count = len(str(stone))
    if stone == 0:
         return blink_n(1, n-1)
    
    if digit_count % 2 == 0:
            exponent = int(digit_count / 2)
            first_stone  = int(stone / math.trunc(math.pow(10, digit_count/2)))
            second_stone = int(stone % math.pow(10, exponent))
            return blink_n(first_stone, n-1) + blink_n(second_stone, n-1)
    
    return blink_n(stone*2024, n-1)

    
print(sum(blink_n(x, 75) for x in stones))
reduce(operator.add, (blink_n(x, 75) for x in stones), 0)
# for n in sorted(blinked.keys()):
#     print(n, blinked[n])

# print(stones)

# blink(stones) #1
# print("1 time", stones)

# blink(stones) #2
# print("2 time", stones)

# blink(stones) #3
# print("3 time", stones)

"""j = 0
while j < 40:
    pre = time()
    blink(stones)
    after = time()
    in_ms = int((after - pre) * 1000)
    print(f"{j}: {in_ms}, num stones: {len(stones)}")
    # print("After ", j, "blinks", stones)
    j+=1
"""





