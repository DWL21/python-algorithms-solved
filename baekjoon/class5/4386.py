import math

n = int(input())
stars = []
for _ in range(n):
    stars.append(tuple(map(float, input().split())))
edges = []
for i in range(n):
    for j in range(i + 1, n):
        distance = math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
        edges.append((distance, i, j))
edges.sort()

parents = [i for i in range(n + 1)]


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

cost = 0
for distance, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        cost += distance


def custom_round(n):
    if (n * 1000) % 10 >= 5:
        return (int(n * 100) + 1) / 100
    return int(n * 100) / 100


print(custom_round(cost))
