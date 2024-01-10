import sys

INF = int(1e9)


input = sys.stdin.readline


n = int(input())
m = int(input())
routes = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    routes[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    routes[a][b] = min(routes[a][b], c)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if i == j or j == k or k == i:
                continue
            cost = routes[j][i] + routes[i][k]
            if routes[j][k] > cost:
                routes[j][k] = cost
                

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if routes[i][j] == INF:
            routes[i][j] = 0
            
for i in range(1, n + 1):
    print(" ".join(map(str, routes[i][1:])))
