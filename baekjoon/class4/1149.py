N = int(input())
houses = []
for _ in range(N):
    houses.append(tuple(map(int, input().split())))
dp = []
dp.append(houses[0])
for i, value in enumerate(houses[1:]):
    i += 1
    r, g, b = value
    x, y, z = dp[i - 1]
    r += min(y, z)
    g += min(x, z)
    b += min(x, y)
    dp.append((r, g, b))
print(min(dp[-1]))

