from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
result = []
for i in range(1, N + 1):
    if not indegree[i]:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)

print(' '.join(map(str, result)))
