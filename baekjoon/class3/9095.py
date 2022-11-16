n = int(input())

dp = [0, 1, 2, 4]
for _ in range(7):
    dp.append(dp[-1] + dp[-2] + dp[-3])

for _ in range(n):
    print(dp[int(input())])
