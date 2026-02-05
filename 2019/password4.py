# 1) 6 digit number
# 2) 2 adjancent digits are the same (like 22 in 122345)
# 3) left to right digits never decrease -> they only increase or stay the same

# INPUT: value in range of 152085-670283

# Q : HOW MANY DIFFERENT PASSWORDS within the range of input meet these criteria?

from pathlib import Path

input_str = Path(__file__).parent / "input.txt"
data = input_str.read_text().strip().splitlines()

def adjacent_digits(arr):
    s = str(arr)
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return True
    return False      
        
def digits_ascending(arr):
    s = str(arr)
    for i in range(len(s)):
        if i == 0:
            continue
        elif s[i] < s[i - 1]:
            return False
    return True

    
print(data)
for lines in data:
    min = int(data[0][:6])
    max = int(data[0][7:])

print("min:", min, type(min))
print(max)

password = min
password_array = []
# print(password) 152085-670283
while min <= password and password < max:
    if adjacent_digits(password) and digits_ascending(password):
        password_array.append(bool(password))
    # print(password_array)
    password += 1
    #print(password)
    # print("password:", password, type(password))
print("number of different passwords within the range 152085-670283:", len(password_array)) 
# print(f"12345 has adjacent equal digits?", {adjacent_digits('12345')}) # false 
# print(f"12345 has ascending digits?", {digits_ascending('12345')}) # true
# print()
# print(f"{password} has adjacent equal digits?", {adjacent_digits(password)}) # false # 152 085
# print(f"{password} has ascending digits?", {digits_ascending(password)}) # false
# print()
# print(f"12245 has adjacent equal digits?", {adjacent_digits('12245')}) # true
# print(f"12245 has ascending digits?", {digits_ascending('12245')}) # true
# print()
# print(f"12243 has adjacent equal digits?", {adjacent_digits('12243')}) # true
# print(f"12243 has ascending digits?", {digits_ascending('12243')}) # false

    
        
    
# 155667
# 155668
# 155669
# 155678
# 155679
# 155689


