import sys

input = sys.stdin.readline


def solution(words: list) -> list:
    return sorted(words, key=lambda x: (len(x[0]), x[0]))


N = int(input())
words = []
for _ in range(N):
    words.append(input().rstrip())
for i in solution(words):
    print(i)
