import sys

input = sys.stdin.readline

N, K = map(int, input().split())
stocks = []
for _ in range(N):
    stocks.append(tuple(map(int, input().split())))
stocks.sort(key=lambda x: (-x[1], x[0]))
queue = []
for weight, value in stocks:
    if weight > K:
        continue
    result = []
    for w, v in list(queue):
        if w + weight <= K:
            result.append((w + weight, v + value))
    result.append((weight, value))
    queue = result
queue.sort(key=lambda x: -x[1])
print(queue)
