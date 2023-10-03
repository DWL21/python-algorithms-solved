def solution(n):
    return len(list(filter(lambda x: not n % x, range(1, n + 1))))
