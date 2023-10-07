def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def is_prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(a, b):
    denominator = b // gcd(a, b)
    for i in range(2, denominator + 1):
        if denominator % i == 0 and i not in [2, 5] and is_prime_number(i):
            return 2
    return 1
