from collections import deque


N, K = map(int, input().split())

routes = [100000] * 1000001
visited = [False] * 100001
queue = deque([N])
routes[N] = 0
while queue:
    n = queue.popleft()
    if visited[K]:
        break
    if visited[n]:
        continue
    visited[n] = True
    k = n * 2
    if k >= 1:
        while k <= 100000 and routes[k] == 100000:
            routes[k] = routes[n]
            queue.append(k)
            k *= 2
    for i in [n - 1, n + 1]:
        if i >= 0 and i <= 100000:
            routes[i] = min(routes[i], routes[n] + 1)
            queue.append(i)
print(routes[K])
