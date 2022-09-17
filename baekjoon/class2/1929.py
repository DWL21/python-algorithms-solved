M, N = map(int, input().split())

is_primes = [True for i in range(N + 1)]
is_primes[1] = False
for i in range(2, N + 1):
    if is_primes[i]:
        j = 2
        while i * j <= N:
            is_primes[i * j] = False
            j += 1
for i in range(M, N + 1):
    if is_primes[i]:
        print(i)
