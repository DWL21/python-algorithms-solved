import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
arrays = []
for _ in range(N):
    arrays.append(list(map(int, map(str, input().strip()))))

houses = []
for i, array in enumerate(arrays):
    for j, value in enumerate(array):
        if value == 1:
            houses.append((i, j))

answer = []
for x, y in houses:
    if arrays[x][y] == 0:
        continue
    queue = deque([(x, y)])
    visited = 0
    while queue:
        i, j = queue.popleft()
        target = [(x, y) for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)] if
                  0 <= x < N and 0 <= y < N and arrays[x][y] == 1]
        for x, y in target:
            queue.append((x, y))
            visited += 1
            arrays[x][y] = 0
    if visited == 0:
        answer.append(1)
    else:
        answer.append(visited)

print(len(answer))
answer.sort()
for i in answer:
    print(i)
