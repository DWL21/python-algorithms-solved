import math
import heapq
import sys


input = sys.stdin.readline

INF = math.inf

N = int(input())
M = int(input())
cities = [[INF] * N for _ in range(N)]
distances = [INF] * N
for _ in range(M):
    departure, arrival, cost = map(int, input().split())
    cities[departure - 1][arrival - 1] = min(cost, cities[departure - 1][arrival - 1])
for i in range(N):
    cities[i][i] = 0
departure, arrival = map(lambda x: int(x) - 1, input().split())
heap = []
heapq.heappush(heap, (0, departure))
distances[departure] = 0

while heap:
    distance, now = heapq.heappop(heap)
    if distances[now] < distance:
        continue
    for i, value in enumerate(cities[now]):
        cost = distance + value
        if cost < distances[i]:
            heapq.heappush(heap, (cost, i))
            distances[i] = cost

print(distances[arrival])

