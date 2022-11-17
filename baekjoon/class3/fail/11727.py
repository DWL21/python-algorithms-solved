dp = [0, 1, 2]

n = int(input())
for _ in range(2 * n):
    dp.append(dp[-2] + dp[-1])
if n == 1 or n == 2:
    dp = [0, 1, 3]
    print(dp[n])
else:
    print(dp[n] + dp[2 * (n - 2)])

