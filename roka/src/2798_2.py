import sys
import itertools

input = sys.stdin.readline


def solution(n: int, m: int, cards: list) -> int:
    return max(
        filter(lambda x: x <= m, 
        map(sum, itertools.combinations(cards, 3))))


N, M = map(int, input().split())
cards = list(map(int, input().split()))
print(solution(N, M, cards))
