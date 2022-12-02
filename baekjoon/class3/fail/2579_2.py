

def solve(N, stairs):
    if N == 1:
        return stairs[1]
    dp = [(0, 0)] * (N + 1)
    dp[1] = (1, stairs[1])
    dp[2] = (2, stairs[1] + stairs[2])
    for i in range(3, N - 1):
        counting_one, value_one = dp[i - 1]
        counting_two, value_two = dp[i - 2]
        if counting_one <= 1 and value_one > value_two:
            dp[i] = (counting_one + 1, value_one + stairs[i])
        else:
            dp[i] = (1, value_two + stairs[i])
    return max(dp[N - 3][1] + stairs[N - 1] + stairs[N], dp[N - 2][1] + stairs[N])


N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))
print(solve(N, stairs))
