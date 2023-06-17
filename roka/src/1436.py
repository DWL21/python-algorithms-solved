import sys

input = sys.stdin.readline


def solution(n: int) -> int:
    counting = 0
    i = 665
    while counting < n:
        i += 1
        if str(i).count("666") >= 1:
            counting += 1
    return i


N = int(input())
print(solution(N))
