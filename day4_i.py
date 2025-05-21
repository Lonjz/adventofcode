maze = []

directions = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]

with open("day_4_input.txt", "r") as files:
    for line in files:
        maze.append(line)

word = "XMAS"

answer = 0

for i in range(len(maze)):
    for j in range(len(maze[0])):
        for [x, y] in directions:
            legit = True
            for k in range(len(word)):
                ni = i + x * k
                nj = j + y * k
                if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]):
                    if maze[ni][nj] != word[k]:
                        legit = False
                        break
                else:
                    legit = False
                    break
            if legit:
                answer += 1

print(answer)