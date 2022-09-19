import sys

input = sys.stdin.readline

K, N = map(int, input().split())
numbers = list()
for _ in range(K):
    numbers.append(int(input()))

minimum = min(numbers)
for i in range(minimum, 0, -1):
    n = 0
    for j in numbers:
        n += j // i
    if n >= N:
        print(i)
        break
