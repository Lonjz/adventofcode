mp_left = {}
mp_right = {}

with open("day_1_input.txt", "r") as files:
    for line in files:
        line = line.split()
        if int(line[0]) in mp_left:
            mp_left[int(line[0])] += 1
        else:
            mp_left[int(line[0])] = 1

        if int(line[1]) in mp_right:
            mp_right[int(line[1])] += 1
        else:
            mp_right[int(line[1])] = 1

answer = 0

for key, val in mp_left.items():
    if key in mp_right:
        answer += key * val * mp_right[key]

print(answer)