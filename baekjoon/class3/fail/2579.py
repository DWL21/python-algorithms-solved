import sys

input = sys.stdin.readline

N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))

DP = [(0, 0) for _ in range(N + 1)]
DP[1] = (stairs[1], 1)
DP[2] =
