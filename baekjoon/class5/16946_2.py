from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().strip())))



dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def get_next_steps(x, y, N, M):
    directions = []
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M or board[new_x][new_y]:
            continue
        directions.append((new_x, new_y))
    return directions

visited = [[0] * M for _ in range(N)]
cycle = [0] * (M * N + 1)
def dfs(start, first, N, M):
    x, y = start

    stack = [start]
    while stack:
        now = stack.pop()
        x, y = now
        if board[x][y] or visited[x][y]:
            continue
        cycle[first] += 1
        visited[x][y] = first
        stack.extend(get_next_steps(x, y, N, M))
    

first = 1
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            now = i, j
            dfs(now, first, N, M)
            first += 1

score = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j]:
            score[i][j] += 1
            points = []
            for x, y in get_next_steps(i, j, N, M):
                points.append(visited[x][y])
            for now in list(set(points)):
                score[i][j] += cycle[now]
            score[i][j] = score[i][j] % 10


for i in score:
    print(''.join(map(str, i)))
    