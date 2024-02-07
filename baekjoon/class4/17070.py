from collections import defaultdict
from collections import deque

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

final = [(N - 1, N - 2, N - 1, N - 1), (N - 2, N - 2, N - 1, N - 1), (N - 2, N - 1, N - 1, N - 1)]
start = (0, 0, 0, 1)
queue = deque([start])
visited = defaultdict(list)

dx1 = [0, 0, 1, 1, 1, 1, 1]
dy1 = [1, 1, 0, 0, 1, 1, 1]
dx2 = [0, 1, 1, 1, 0, 1, 1]
dy2 = [1, 1, 0, 1, 1, 0, 1]

directions = [(0, 2), (2, 4), (4, 7)]


def is_allowed(a, N):
    if a < 0 or N <= a:
        return False
    return True


def loop(numbers, N):
    for i in numbers:
        if not is_allowed(i, N):
            return False
    return True

while queue:
    x1, y1, x2, y2 = queue.popleft()
    if x1 == x2 and y1 + 1 == y2:
        a, b = directions[0]
    elif x1 + 1 == x2 and y1 == y2:
        a, b = directions[1]
    elif x1 + 1 == x2 and y1 + 1 == y2:
        a, b = directions[2]
    for i in range(a, b):
        new = (x1 + dx1[i], y1 + dy1[i], x2 + dx2[i], y2 + dy2[i])
        if not loop(new, N) or board[new[2]][new[3]] or (dx2[i] == 1 and dy2[i] == 1 and (board[new[0] + 1][new[1]] or board[new[0]][new[1] + 1])):
            continue
        now = x1, y1, x2, y2
        if now not in visited[new]:
            visited[new].append((x1, y1, x2, y2))
            queue.append(new)

stack = list(final)
total = 0

for i in visited.keys():
    visited[i] = list(set(visited[i]))

while stack:
    now = stack.pop()
    if now == start:
        total += 1
    else:
        stack.extend(visited[now])

print(total)
