import sys


input = sys.stdin.readline

V, E = map(int, input().split())
graph = []
for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

parents = [i for i in range(V + 1)]
graph.sort()


def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    parentA = find_parent(a)
    parentB = find_parent(b)
    if parentA < parentB:
        parents[parentB] = parentA
        return
    parents[parentA] = parentB


result = 0
for c, a, b in graph:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += c

print(result)
