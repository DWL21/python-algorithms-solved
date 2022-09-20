import sys

input = sys.stdin.readline

coins = list()
N, K = map(int, input().split())
for _ in range(N):
    coins.append(int(input()))
count = 0
for i in coins[::-1]:
    count += K // i
    K %= i
    if K == 0:
        break
print(count)
