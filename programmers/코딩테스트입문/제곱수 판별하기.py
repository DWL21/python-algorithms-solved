from math import sqrt


def solution(n):
    for i in range(int(sqrt(n)), int(sqrt(n) + 1)):
        if i ** 2 == n:
            return 1
    return 2