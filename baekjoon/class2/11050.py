def factorial(number):
    value = 1
    for i in range(number):
        value *= i + 1
    return value


N, K = map(int, input().split())
answer = factorial(N) // (factorial(N - K) * factorial(K))
print(answer)
