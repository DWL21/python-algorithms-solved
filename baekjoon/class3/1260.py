from collections import defaultdict
from collections import deque

N, M, V = map(int, input().split())

points = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    points[x].append(y)
    points[y].append(x)

for i in points.values():
    i.sort()

stack = [V]
dfs = []
while stack:
    temp = stack.pop()
    if temp not in dfs:
        dfs.append(temp)
        stack.extend(reversed(points[temp]))
print(" ".join(map(str, dfs)))

queue = deque([V])
bfs = []
while queue:
    temp = queue.popleft()
    if temp not in bfs:
        bfs.append(temp)
        queue.extend(points[temp])
print(" ".join(map(str, bfs)))
