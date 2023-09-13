def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def to_times(m, n, x, y):
    maximum = lcm(m, n)
    times = x
    while times <= maximum:
        if (times - 1) % n + 1 == y:
            return times
        times += m 
    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(to_times(M, N, x, y))

