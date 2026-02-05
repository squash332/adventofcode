# 1) 6 digit number
# 2) 2 adjancent digits are the same (like 22 in 122345)
# 3) left to right digits never decrease -> they only increase or stay the same

# INPUT: value in range of 152085-670283

# Q : HOW MANY DIFFERENT PASSWORDS within the range of input meet these criteria?
from collections import Counter
from pathlib import Path

input_str = Path(__file__).parent / "input.txt"
data = input_str.read_text().strip().splitlines()

def adjacent_digits(arr):
    s = str(arr)
    counts = Counter(s)
    return 2 in counts.values()   
        
def digits_ascending(arr):
    s = str(arr)
    for i in range(len(s) - 1):
        if s[i + 1] < s[i]:
            return False
    return True

print(data)
for lines in data:
    min = int(data[0][:6])
    max = int(data[0][7:])

password = min
password_array = []
# print(password) 152085-670283
while min <= password and password < max:
    if adjacent_digits(password) and digits_ascending(password):
        password_array.append(password)
    password += 1
print("number of different passwords within the range <152085,670283>:", len(password_array)) 

