N = int(input())

remainder = 1000000007

dp = {0: 0, 1: 1, 2: 1, 3: 2}


def fi(n):
    if n in dp.keys():
        return dp[n]
    if n % 2:
        dp[n] = (fi(n // 2 + 1) ** 2 + fi(n // 2) ** 2) % remainder
        return dp[n]
    dp[n] = (fi(n // 2) * (fi(n // 2) + 2 * fi(n // 2 - 1))) % remainder
    return dp[n]


print(fi(N) % remainder)

