def factorial(n):
    answer = 1
    for i in range(2, n + 1):
        answer *= i
    return answer


def solution(balls, share):
    answer = factorial(balls) // factorial(balls - share) // factorial(share)
    return answer
