import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
tomato_fields = []
for _ in range(N):
    tomato_fields.append(list(map(int, input().split())))

initial_tomatoes = deque()
for row, tomatoes in enumerate(tomato_fields):
    for column, tomato in enumerate(tomatoes):
        if tomato == 1:
            initial_tomatoes.append((row, column))
for i in list(initial_tomatoes):
    while initial_tomatoes:
        row, column = initial_tomatoes.popleft()
        route = [(x, y) for x, y in [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)] if
                 0 <= x < N and 0 <= y < M and tomato_fields[x][y] == 0]
        for x, y in route:
            tomato_fields[x][y] = tomato_fields[row][column] + 1
            initial_tomatoes.append((x, y))

for i in tomato_fields:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
print(max(map(max, tomato_fields)) - 1)
