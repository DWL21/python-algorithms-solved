import sys

input = sys.stdin.readline

def solution(n: int) -> int:
    for i in range(1, n):
        if sum(map(int, str(i))) + i == n:
            return i
    return 0


N = int(input())
print(solution(N))
