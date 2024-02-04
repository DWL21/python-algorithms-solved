from itertools import combinations
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
blanks = []
bugs = []
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            blanks.append((i, j))
        elif board[i][j] == 2:
            bugs.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cases = list(combinations(blanks, 3))
maximum = 0
for i in cases:
    now_board = deepcopy(board)
    for x, y in i:
        now_board[x][y] = 1
    visited = [[False] * M for _ in range(N)]
    queue = deque(bugs)
    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for j in range(4):
            new_x = x + dx[j]
            new_y = y + dy[j]
            if 0 <= new_x and new_x < N and 0 <= new_y and new_y < M and not now_board[new_x][new_y]:
                now_board[new_x][new_y] = 2
                queue.append((new_x, new_y))
    result = 0
    for x in range(N):
        for y in range(M):
            if not now_board[x][y]:
                result += 1
    maximum = max(maximum, result)

print(maximum)
 
