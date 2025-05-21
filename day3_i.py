import re

seq = ""

with open("day_3_input.txt", "r") as files:
    seq = files.read()
    
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

found = re.findall(pattern, seq)

answer = 0

for val in found:
    try:
        answer += abs(int(val[0])) * abs(int(val[1]))
    except ValueError as e:
        answer += 0

print(answer)