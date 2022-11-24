N, R, C = map(int, input().split())


def where_is(n, r, c):
    count_plus = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): 2,
        (1, 1): 3
    }
    if n == 1:
        return count_plus[(r, c)]
    return count_plus[r // (2 ** (n - 1)), c // (2 ** (n - 1))] * (2 ** (2 * n - 2)) + where_is(n - 1, r % (2 ** (n - 1)), c % (2 ** (n - 1)))


print(where_is(N, R, C))
