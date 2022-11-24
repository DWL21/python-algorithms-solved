import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def solution(M):
    if M == 0:
        return 1
    lines = defaultdict(list)
    for _ in range(M):
        x, y = map(int, input().split())
        lines[x].append(y)
        lines[y].append(x)
    counting = 0
    histories = [0] * (N + 1)
    for i in lines.keys():
        if histories[i]:
            continue
        queue = deque([i])
        while queue:
            n = queue.popleft()
            if not histories[n]:
                histories[n] = 1
                queue.extend(lines[n])
                lines[n].clear()
        counting += 1
    return counting + (N - sum(histories))


N, M = map(int, input().split())
print(solution(M))
