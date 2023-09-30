from collections import deque, defaultdict

def solution(A, B):
    queue = deque([(A, 1)])
    is_visited = defaultdict(bool)
    while queue:
        number, times = queue.popleft()
        if is_visited[number]:
            continue
        is_visited[number] = True
        for i in [number * 2, number * 10 + 1]:
            if i == B:
                return times + 1
            elif i < B:
                queue.append((i, times + 1))
    return -1

A, B = map(int, input().split())
print(solution(A, B))
