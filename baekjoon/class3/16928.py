from collections import defaultdict
from collections import deque

routes = defaultdict(list)
ladders = [False] * 101
N, M = map(int, input().split())


def solution(routes, ladders):
    queue = deque([1])
    visited = [False] * 101
    times = [0] * 101
    while queue:
        departure = queue.popleft()
        for i in routes[departure]:
            if i == 100:
                return times[departure] + 1
            if visited[i]:
                continue
            visited[i] = True
            if ladders[i]:
                destination = routes[i][0]
                visited[destination] = True
            else:
                destination = i
            if times[destination] == 0:
                times[destination] = times[departure] + 1
                queue.append(destination)
                
                    
for i in range(1, 100):
    routes[i].extend([i + j + 1 for j in range(6) if i + j < 100])
for _ in range(N + M):
    x, y = map(int, input().split())
    routes[x] = [y]
    ladders[x] = True
print(solution(routes, ladders))

