import heapq
import sys
from collections import defaultdict

INF = int(1e9)
input = sys.stdin.readline


N, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 =  map(int, input().split())

def dijkstra(graph, start):
    distances = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (start, 0))
    while q:
        now, distance = heapq.heappop(q)
        if distances[now] < distance:
            continue
        for target, target_distance in graph[now]:
            cost = distance + target_distance
            if cost < distances[target]:
                distances[target] = cost
                heapq.heappush(q, (target, cost))
    return distances


def has_route(a):
    if a > int(1e8):
        return False
    return True


a = dijkstra(graph, 1)
b = dijkstra(graph, v1)
c = dijkstra(graph, v2)

x = a[v1]
y = a[v2]

z = b[v2]

d1 = b[N]
d2 = c[N]


if v1 == 1 and v2 == N:
    answer = y
elif v1 == 1:
    answer = y + d2
elif v2 == N:
    answer = x + d1
else:
    answer = min(x + z + d2, y + z + d1, x + 2*z + d1, y + 2*z + d2)

if has_route(answer):
    print(answer)
else:
    print(-1)
