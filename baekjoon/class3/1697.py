from collections import defaultdict
from collections import deque


def solution(N, K):
    bfs = defaultdict(list)
    if N >= K:
        return N - K
    max_length = 100000
    for i in range(max_length + 1):
        bfs[i].extend([j for j in [i - 1, i + 1, i * 2] if 0 <= j <= max_length])
    visited = [False] * (max_length + 1)
    queue = deque([(N, 0)])
    minimum_counting = set()
    while queue:
        number, counting = queue.popleft()
        if number == K:
            minimum_counting.add(counting)
        if not visited[number]:
            queue.extend(list(map(lambda it: (it, counting + 1), bfs[number])))
            visited[number] = True
    return min(minimum_counting)


N, K = map(int, input().split())
print(solution(N, K))
