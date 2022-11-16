dp = [0, 1, 1, 1, 2, 2]

for _ in range(95):
    dp.append(dp[-5] + dp[-1])

n = int(input())
for _ in range(n):
    print(dp[int(input())])
