from collections import deque

N = int(input())
routes = []
answer = [[0] * N for _ in range(N)]
for _ in range(N):
    routes.append(list(map(int, input().split())))

for i in range(N):
    queue = deque()
    for j, road in enumerate(routes[i]):
        if road:
            queue.append((i, j))
    visited = [[0] * N for _ in range(N)]
    while queue:
        x, y = queue.popleft()
        if not visited[x][y]:
            visited[x][y] = 1
            answer[i][y] = 1
            for j, road in enumerate(routes[y]):
                if road:
                    queue.append((y, j))   
for i in answer:
    print(" ".join(map(str, i)))
