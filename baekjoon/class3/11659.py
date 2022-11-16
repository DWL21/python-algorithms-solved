import sys

input = sys.stdin.readline


N, M = map(int, input().split())
numbers = list(map(int, input().split()))

maximum = 0
answer = [0]
for i in numbers:
    maximum += i
    answer.append(maximum)

for _ in range(M):
    start, end = map(int, input().split())
    if start == end:
        print(answer[end] - answer[start - 1])
    else:
        print(answer[end] - answer[start - 1])
