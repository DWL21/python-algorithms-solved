from collections import defaultdict

N, K = map(int, input().split())
stuffs = []
for _ in range(N):
    stuffs.append(tuple(map(int, input().split())))

dp = [[0] * len(stuffs) for _ in range(K + 1)]
for i in range(len(stuffs)):
    w, v = stuffs[i]
    for j in range(K + 1):
        if w > j:
            dp[j][i] = dp[j][i - 1]
        else:
            dp[j][i] = max(dp[j][i - 1], v + dp[j - w][i - 1])
print(dp[-1][-1])

