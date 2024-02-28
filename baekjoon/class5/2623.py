from collections import defaultdict
from collections import deque

N, M = map(int, input().split())
graph = defaultdict(list)
indegree = [0] * (N + 1)
for _ in range(M):
    plan = list(map(int, input().split()[1:]))
    for i, value in enumerate(plan[:-1]):
        graph[value].append(plan[i + 1])
        indegree[plan[i + 1]] += 1

q = deque()
answer = []
visited = [False] * (N + 1)
for i in range(1, N + 1):
    if not indegree[i]:
        q.append(i)
while q:
    now = q.popleft()
    answer.append(now)
    visited[now] = True
    for i in graph[now]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)


print(visited)
