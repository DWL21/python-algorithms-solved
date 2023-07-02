def factorial(n: int) -> int:
    if n == 0:
        return 1
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


N = int(input())
print(factorial(N))

