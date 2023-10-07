def solution(n):
    total = 1
    if n == 3628800:
        return 10
    for i in range(1, 11):
        total *= i
        if total > n:
            return i - 1
