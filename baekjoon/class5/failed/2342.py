from itertools import permutations

dances = list(map(int, input().split()))[:-1]
dp = [[int(1e5)] * 10 for _ in range(len(dances))]


def calculate_weight(start, end):
    if start == end:
        return 1
    if not start:
        return 2
    if max(start, end) - min(start, end) in [1, 3]:
        return 3
    return 4


cases = list(permutations(range(5), 2))
index = dict()
for i in range(len(cases)):
    index[cases[i]] = i

dp[0][index[0, dances[0]]] = calculate_weight(0, dances[0])
dp[0][index[dances[0], 0]] = calculate_weight(0, dances[0])

for i in range(1, len(dances)):
    for j in range(10):
        now = dances[i]
        x, y = cases[j]
        if now in cases[j]:
            dp[i][j] = dp[i - 1][index[x, y]] + 1
        else:
            dp[i][j] = min(dp[i - 1][index[x, now]] + calculate_weight(y, now), dp[i - 1][index[now, y]] + calculate_weight(x, now))
for i in dp:
    print(' '.join(map(str, i)))
        