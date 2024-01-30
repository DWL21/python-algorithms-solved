from itertools import combinations


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
cities = []
chickens = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            cities.append((i, j))
        elif board[i][j] == 2:
            chickens.append((i, j))
distances = [[0] * len(cities) for _ in range(len(chickens))]
for i, (x, y) in enumerate(chickens):
    for j, (a, b) in enumerate(cities):
        distances[i][j] = abs(x - a) + abs(y - b)

minimum = int(1e9)
for case in list(combinations(distances, M)):
    minimum = min(minimum, sum(map(min, list(zip(*case)))))
print(minimum)
