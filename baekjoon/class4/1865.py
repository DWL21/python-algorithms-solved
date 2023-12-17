import sys


INF = int(1e4 + 1)

input = sys.stdin.readline

def bellman_ford(graph, start, N):
    distances = [INF] * (N + 1)
    distances[start] = 0
    for _ in range(N - 1):
        for i, value in enumerate(graph[1:]):
            for j, T in value:
                cost = distances[i + 1] + T
                if distances[j] > cost:
                    distances[j] = cost
    for i, value in enumerate(graph[1:]):
            for j, T in value:
                cost = distances[i + 1] + T
                if distances[j] > cost:
                    return True
    return False
    

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    lines = [[] for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        lines[S].append((E, T))
        lines[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        lines[S].append((E, -T))
    if bellman_ford(lines, 1, N):
        print("YES")
    else:
        print("NO")

