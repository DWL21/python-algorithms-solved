import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(str, input().strip())))

directions = dict()
UP = 'U'
LEFT = 'L'
DOWN = 'D'
RIGHT = 'R'
directions[UP] = (-1, 0)
directions[LEFT] = (0, -1)
directions[DOWN] = (1, 0)
directions[RIGHT] = (0, 1)

cycle = [0]
visited = defaultdict(int)

def dfs(now, first):
    if visited[now] == first:
        cycle[0] += 1
        return
    if visited[now]:
        return
    
    visited[now] = first
    x, y = now
    dx, dy = directions[board[x][y]]
    next = (x + dx, y + dy)
    dfs(next, first)

first = 1
for i in range(N):
    for j in range(M):
        dfs((i, j), first)
        first += 1
    
print(cycle[0])
