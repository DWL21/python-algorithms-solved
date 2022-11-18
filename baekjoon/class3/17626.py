import math
import sys

dp = [0, 1]

n = int(input())
for i in range(2, n + 1):
    minimum = sys.maxsize
    i_sqrt = int(math.sqrt(i))
    if i == i_sqrt ** 2:
        dp.append(1)
        continue
    for j in range(1, i_sqrt + 1):
        jj = j ** 2
        minimum = min(dp[jj] + dp[i - jj], minimum)
    dp.append(minimum)
print(dp[n])
