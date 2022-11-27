from collections import defaultdict, deque

N, M = map(int, input().split())
bfs = defaultdict(list)
friends = defaultdict(int)
for _ in range(M):
    x, y = map(int, input().split())
    bfs[x].append(y)
    bfs[y].append(x)
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        queue = deque([i])
        visited = [0] * (N + 1)
        while queue:
            n = queue.popleft()
            if j == n:
                friends[i] += visited[n]
                friends[j] += visited[n]
                break
            for k in bfs[n]:
                if not visited[k]:
                    queue.append(k)
                    visited[k] += visited[n] + 1
answer = sorted(list(friends.items()), key=lambda it: (it[1], it[0]))
print(answer.pop(0)[0])
