import sys

N = int(input())
DP = [sys.maxsize for _ in range(max(4, N + 1))]
DP[1] = 0
DP[2] = 1
DP[3] = 1
if not N <= 3:
    for i in range(4, N + 1):
        temp = list()
        if i % 3 == 0:
            temp.append(DP[i // 3])
        if i % 2 == 0:
            temp.append(DP[i // 2])
        temp.append(DP[i - 1])
        now = min(temp) + 1
        DP[i] = now
print(DP[N])
