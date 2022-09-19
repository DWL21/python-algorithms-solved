import sys

input = sys.stdin.readline

numbers = list()
K, N = map(int, input().split())
for _ in range(K):
    numbers.append(int(input()))

success = True

left = 1
right = max(numbers)
while left <= right:
    middle = (left + right) // 2
    count = sum(map(lambda x: x // middle, numbers))
    if count < N:
        right = middle - 1
    else:
        left = middle + 1

print(right)
