dp = [0, 1, 2]
n = int(input())
for _ in range(n - 2):
    dp.append(dp[-2] + dp[-1])
print(dp[n] % 10007)
