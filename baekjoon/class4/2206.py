from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
	board.append(list(map(int, input())))

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = int(1e9)


def make_routes(now, board, N, M):
    routes = []
    x, y, distance, breaking = now
    for l, m in directions:
        x_goto = x + l
        y_goto = y + m
        if 0 > x_goto or x_goto >= N or 0 > y_goto or y_goto >= M:
            continue
        if board[x_goto][y_goto] and breaking:
            routes.append((x_goto, y_goto, distance + 1, False))
            continue
        if not board[x_goto][y_goto]:
            routes.append((x_goto, y_goto, distance + 1, breaking))
    return routes


visited = [[False] * M for _ in range(N)]
breaking_visited = [[False] * M for _ in range(N)]

answer = INF
start = (0, 0, 0, True)
queue = deque([start])

while queue:
    now = queue.popleft()
    x, y, distance, breaking = now
    if (x, y) == (N - 1, M - 1):
        answer = min(answer, distance)
        continue
    if (not breaking and visited[x][y]) or (breaking and breaking_visited[x][y]):
        continue
    if breaking:
        breaking_visited[x][y] = True
    else:
        visited[x][y] = True
    queue.extend(make_routes(now, board, N, M))


if answer < INF:
    print(answer + 1)
else:
    print(-1)
    
