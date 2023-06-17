import sys

input = sys.stdin.readline


def solution(coefficients: list) -> list:
    a, b, c, d, e, f = map(int, coefficients)
    x = (c*e-b*f)//(a*e-b*d)
    y = (a*f-d*c)//(a*e-b*d)
    return [x, y]


coefficients = list(map(int, input().split()))
print(" ".join(map(str, solution(coefficients))))
