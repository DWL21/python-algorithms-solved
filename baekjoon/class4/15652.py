from itertools import combinations_with_replacement


def solution(N, M):
    return list(combinations_with_replacement(range(1, N + 1), M))
    

N, M = map(int, input().split())
for case in solution(N, M):
    print(" ".join(map(str, case)))
