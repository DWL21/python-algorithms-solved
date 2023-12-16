import sys

from collections import defaultdict
from collections import deque


input = sys.stdin.readline

N = int(input())
trees = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)

visited = [False] * (N + 1)
parents = [0] * (N + 1)
stack = [1]
while stack:
    now = stack.pop()
    if visited[now]:
        continue
    visited[now] = True
    for i in trees[now]:
        if not parents[i]:
            parents[i] = now
            stack.append(i)
for i in parents[2:]:
    print(i)
