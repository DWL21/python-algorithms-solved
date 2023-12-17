from collections import deque
from collections import defaultdict
import heapq

INF = int(1e9)
N, M, X = map(int, input().split())
graph1 = [[] * (N + 1) for _ in range(N + 1)]
graph2 = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    departure, arrival, time = map(int, input().split())
    graph1[departure].append((arrival, time))
    graph2[arrival].append((departure, time))


def dijkstra(graph, N, X):
    distances = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, X))
    while q:
        time, now = heapq.heappop(q)
        if distances[now] < time:
            continue
        for arrival, time_arrival in graph[now]:
            cost = time_arrival + time
            if cost < distances[arrival]:
                distances[arrival] = cost
                heapq.heappush(q, (cost, arrival))
    return distances

first = dijkstra(graph1, N, X)
second = dijkstra(graph2, N, X)
answer = list(map(lambda x: first[x] + second[x], range(1, N + 1)))
answer.pop(X - 1)
print(max(answer))
