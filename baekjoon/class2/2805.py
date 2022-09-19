import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
M = sum(trees) - M

finished = True
left = 0
right = max(trees)
while left <= right:
    H = (left + right) // 2
    target_trees = list(filter(lambda x: x <= H, trees))
    length = sum(target_trees) + H * (len(trees) - len(target_trees))
    if length > M:
        right = H - 1
    elif length < M:
        left = H + 1
    else:
        print(H)
        finished = False
        break

if finished:
    print(right)
