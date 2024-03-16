import math

def solution(a):
    return int(math.sqrt(4*a + 1))


n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    now = y - x
    print(solution(now - 1))
