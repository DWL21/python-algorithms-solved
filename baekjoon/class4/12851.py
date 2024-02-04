from collections import deque
from collections import defaultdict

INF = int(1e8)

N, K = map(int, input().split())
parents = defaultdict(list)
distances = [INF] * (int(1e5) + 1)
queue = deque([N])
distances[N] = 0
while queue:
    now = queue.popleft()
    if now == K:
        continue
    for i, j in [(now - 1, 0), (now + 1, 1), (now * 2, 2)]:
        if i < 0 or int(1e5) < i:
            continue
        distance = distances[now] + 1
        if distance < distances[i]:
            parents[i] = [(now, j)]
            distances[i] = distance
            queue.append(i)
        elif distance == distances[i]:
            parents[i].append((now, j))
            distances[i] = distance
            queue.append(i)


def count_root(K, N):
    result = 0
    stack = list(parents[K])
    while stack:
        now, j = stack.pop()
        if now == N:
            result += 1
        else:
            stack.extend(parents[now])
    return result

for i in parents.keys():
    parents[i] = list(set(parents[i]))
    
if K == N:
    print(0)
    print(1)
else:
    print(distances[K])
    print(count_root(K, N))


for i in range(15):
    print(i, ' '.join(map(str, parents[i])))

