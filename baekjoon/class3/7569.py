import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
tomatoes = []
for _ in range(H):
    one_stock = []
    for _ in range(N):
        one_stock.append(list(map(int, input().split())))
    tomatoes.append(one_stock)
stating_points = []

for z, one_stock in enumerate(tomatoes):
    for y, tomato in enumerate(one_stock):
        for x, value in enumerate(tomato):
            if value == 1:
                stating_points.append((z, y, x))

queue = deque(list(filter(lambda it: tomatoes[it[0]][it[1]][it[2]] == 1, stating_points)))
while queue:
    k = queue.popleft()
    target = [(x, y, z) for x, y, z in
              [(k[0] - 1, k[1], k[2]), (k[0] + 1, k[1], k[2]), (k[0], k[1] + 1, k[2]), (k[0], k[1] - 1, k[2]), (k[0], k[1], k[2] - 1), (k[0], k[1], k[2] + 1)] if
              0 <= x < H and 0 <= y < N and 0 <= z < M and tomatoes[x][y][z] == 0]
    for x, y, z in target:
        tomatoes[x][y][z] = tomatoes[k[0]][k[1]][k[2]] + 1
        queue.append((x, y, z))

all = []
for one_stock in tomatoes:
    for tomato in one_stock:
        for value in tomato:
            if value == 0:
                print(-1)
                exit(0)
            all.append(value)
print(max(all) - 1)
