import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lines = []
for _ in range(m):
    lines.append(tuple(map(int, input().split())))

parents = [i for i in range(n)]

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
        return
    parents[a] = b


answer = 1
for x, y in lines:
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        answer += 1
    else:
        break

if answer > m:
    answer = 0

print(answer)
