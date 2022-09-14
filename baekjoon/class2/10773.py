import sys


input = sys.stdin.readline
N = int(input())
answer = []
for _ in range(N):
    now = int(input())
    if now:
        answer.append(now)
    else:
        answer.pop()
print(sum(answer))
