maze = []

with open("day_4_input.txt", "r") as files:
    for line in files:
        maze.append(line.strip())

answer = 0

def isValid(i, j):
    diag1 = maze[i][j] + maze[i+1][j+1] + maze[i+2][j+2]
    diag2 = maze[i][j+2] + maze[i+1][j+1] + maze[i+2][j]
    valid = ["MAS", "SAM"]
    return diag1 in valid and diag2 in valid

for i in range(len(maze) - 2):
    for j in range(len(maze[0]) - 2):
        if isValid(i, j):
            answer += 1

print(answer)