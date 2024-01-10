from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
	board.append(input())

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = int(1e9)


def make_routes(now, board, N, M):
    routes = []
    for l, m in directions:
            x, y, distance, breaking = now
            x_goto = x + l
            y_goto = y + m
            if 0 <= x_goto and x_goto < N and 0 <= y_goto and y_goto < M:
                if board[x_goto][y_goto] == 0:
                    routes.append((x_goto, y_goto, distance + 1, True))
                    continue
                if breaking:
                    routes.append((x_goto, y_goto, distance + 1, False))
    return routes


visited = [[False] * N for _ in range(M)]
breaking_visited = [[False] * N for _ in range(N)]

answer = INF
start = (0, 0, 0, True)
queue = deque([start])

while queue:
    now = queue.popleft()
    print(now)
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


print(answer)
	
