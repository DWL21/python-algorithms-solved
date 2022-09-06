import math


def is_prime_num(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


count = 0
N = int(input())
numbers = list(map(int, input().split()))
for i in numbers:
    if is_prime_num(i):
        count += 1
print(count)
