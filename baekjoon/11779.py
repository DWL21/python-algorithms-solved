from collections import deque
from collections import defaultdict
import heapq

INF = int(1e8)

n = int(input())
m = int(input())
buses = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if buses[a][b] > c:
        buses[a][b] = c
S, D = map(int, input().split())


parents = dict()
distances = [INF] * (n + 1)
q = []
distances[S] = 0
heapq.heappush(q, (0, S))
while q:
    distance, now = heapq.heappop(q)
    if distance <= distances[now]:
        for i, new_distance in enumerate(buses[now]):
            cost = distance + new_distance
            if cost < distances[i]:
                parents[i] = now
                distances[i] = cost
                heapq.heappush(q, (cost, i))
result = distances[D]

path = [D]
now = path[0]
while now in parents:
    now = parents[now]
    path.append(now)
path.reverse()
print(len(path))
print(' '.join(map(str, path)))



