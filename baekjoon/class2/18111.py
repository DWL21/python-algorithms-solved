import sys

input = sys.stdin.readline


max_height = 256
N, M, B = map(int, input().split())
fields = list()
for _ in range(N):
    fields.append(list(map(int, input().split())))
height = 0
minimum_time = sys.maxsize
for i in range(max_height + 1):
    timer = 0
    block = B
    for j in fields:
        for k in j:
            if k > i:
                block += (k - i)
                timer += 2 * (k - i)
            elif k < i:
                block -= (i - k)
                timer += (i - k)
    if 0 <= block and timer <= minimum_time:
        minimum_time = timer
        height = max(height, i)

print(f"{minimum_time} {height}")
