N = int(input())
sequence = list(map(int, input().split()))
dp = [1] * len(sequence)
for i in range(len(sequence)):
    maximum = 1
    for j in range(len(sequence[:i + 1])):
        if sequence[j] < sequence[i]:
            maximum = max(maximum, dp[j] + 1)
    dp[i] = maximum
print(max(dp))

