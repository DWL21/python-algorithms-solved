import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
candies = [0] + list(map(int, input().split()))

edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split())))


parents = [i for i in range(N + 1)]
def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)

groups = [0] * (N + 1)
times = [0] * (N + 1)
for i in range(1, N + 1):
    a = find_parent(i)
    groups[a] += candies[i]
    times[a] += 1

result = []
for i in range(1, N + 1):
    if times[i]:
        result.append((times[i], groups[i]))


dp = [[0] * (K + 1) for _ in range(len(result) + 1)]

for i in range(1, len(result) + 1):
    weight, value = result[i - 1]
    for j in range(1, K + 1):
        if weight >= j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i - 1][j])

print(dp[len(result)][K])
