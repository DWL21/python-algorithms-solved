import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
arrays = []
for _ in range(N):
    arrays.append(list(map(int, map(str, input().strip()))))
queue = deque([(0, 0)])
while queue:
    i, j = queue.popleft()
    if (i, j) == (N - 1, M - 1):
        print(arrays[i][j])
        break
    target = [(x, y) for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)] if 0 <= x < N and 0 <= y < M and arrays[x][y] == 1]
    for x, y in target:
        queue.append((x, y))
        arrays[x][y] = arrays[i][j] + 1
