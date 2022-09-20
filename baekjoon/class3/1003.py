import sys

input = sys.stdin.readline

N = int(input())
cases = []
for _ in range(N):
    num = int(input())
    cases.append(num)

DP = [[0, 0] for _ in range(41)]

DP[0] = [1, 0]
DP[1] = [0, 1]

for i in range(2, max(cases) + 1):
    DP[i][0] = DP[i - 1][0] + DP[i - 2][0]
    DP[i][1] = DP[i - 1][1] + DP[i - 2][1]
for i in cases:
    print(f"{DP[i][0]} {DP[i][1]}")

