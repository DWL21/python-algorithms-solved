import math

def is_prime_number(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return False
    return True


def solution(n):
    answer = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime_number(i):
            answer.append(i)
    return answer
