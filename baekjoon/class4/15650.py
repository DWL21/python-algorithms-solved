from itertools import combinations


def solution(N, M):
    return list(combinations(range(1, N + 1), M))
    

N, M = map(int, input().split())
for case in solution(N, M):
    print(" ".join(map(str, case)))
