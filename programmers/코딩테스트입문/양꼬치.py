LAMB = 12000
DRINK = 2000

def solution(n, k):
    return LAMB * n + DRINK * (k - n // 10)
