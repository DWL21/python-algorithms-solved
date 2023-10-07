from itertools import combinations


def solution(dots):
    [a, b], [c, d], [e, f], [g, h] = dots
    case1 = (c - a) / (d - b) == (g - e) / (h - f)
    case2 = (e - a) / (f - b) == (g - c) / (h - d)
    case3 = (g - a) / (h - b) == (e - c) / (f - d)
    if case1 or case2 or case3:
        return 1
    return 0
