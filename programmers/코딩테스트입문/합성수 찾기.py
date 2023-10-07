import math


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n):
    times = 0
    for i in range(2, n + 1):
        if not is_prime_number(i):
            times += 1
    return times
    