import heapq

left = []
right = []

with open("day_1_input.txt", "r") as files:
    for line in files:
        line = line.split()
        heapq.heappush(left, int(line[0]))
        heapq.heappush(right, int(line[1]))

answer = 0

while len(left) > 0:
    answer += abs(heapq.heappop(left) - heapq.heappop(right))

print(answer)