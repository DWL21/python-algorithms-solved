import sys

input = sys.stdin.readline


def select_cards(n: int) -> list:
  positions = []
  for i in range(n-2):
    for j in range(i+1, n-1):
      for k in range(j+1, n):
        positions.append((i, j, k))
  return positions

def solution(n: int, m: int, cards: list) -> int:
    answer = 0
    for i, j, k in select_cards(n):
        total = cards[i]+cards[j]+cards[k]
        if total == m:
            return m
        if total < m:
            answer = max(total, answer)
    return answer


N, M = map(int, input().split())
cards = list(map(int, input().split()))
print(solution(N, M, cards))
