from collections import defaultdict, deque

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    points = []
    for _ in range(K):
        X, Y = map(int, input().split())
        points.append((X, Y))
    bfs = defaultdict(list)
    for X, Y in points:
        cases = [(x, y) for x, y in [(X, Y - 1), (X, Y + 1), (X - 1, Y), (X + 1, Y)] if (x, y) in points]
        bfs[(X, Y)].extend(cases)
        for x, y in cases:
            bfs[(x, y)].append((X, Y))

    histories = set()
    counting = 0
    for i in bfs.keys():
        if i in histories:
            continue
        queue = deque([i])
        while queue:
            n = queue.popleft()
            if n not in histories:
                queue.extend(bfs[n])
                histories.add(n)
        counting += 1

    print(counting + (K - len(histories)))
