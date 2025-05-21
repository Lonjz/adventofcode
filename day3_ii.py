import re

seq = ""

with open("day_3_input.txt", "r") as files:
    seq = files.read()
    
pattern = re.compile(r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))")
found = pattern.findall(seq)

answer = 0
enable = True

for type, x, y in found:

    if type == "do()":
        enable = True
    
    elif type == "don't()":
        enable = False

    if type.startswith("mul(") and enable:
        answer += abs(int(x)) * abs(int(y))
    

print(answer)