arrays = []

def isValid(arr):
    last = 0
    diff = 0
    badcount = 0
    for i in arr:
        entry = int(i)
        if last == 0:
            last = entry
            continue
        else:
            temp = entry - last
            if abs(temp) < 1 or abs(temp) > 3 or diff*temp < 0:
                return False
            else:
                diff = temp
        last = entry
    return True

with open("day_2_input.txt", 'r') as files:
    for line in files:
        x = line.split()
        arrays.append(x)

answer = 0

for arr in arrays:
    if isValid(arr):
        answer += 1
    else:
        for i in range(len(arr)):
            temp = arr[:i] + arr[i+1:]
            if isValid(temp):
                answer += 1
                break

print(answer)


