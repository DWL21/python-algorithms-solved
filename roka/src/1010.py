def factorial(n: int) -> int:
    if n == 0:
        return 1
    number = 1
    for i in range(2, n + 1):
        number *= i
    return number


def combinations(n: int, m: int) -> int:
    return factorial(m)//(factorial(m - n)*  factorial(n))


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(combinations(N, M))
    
