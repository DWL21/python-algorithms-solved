import math

M, N = map(int, input().split())


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


if M == 1:
    M += 1
for i in range(M, N + 1):
    if is_prime(i):
        print(i)
