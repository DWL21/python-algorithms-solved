import sys
import collections


input = sys.stdin.readline


N, M = map(int, input().rstrip().split())
words = []
for _ in range(N):
    s = input().rstrip()
    if len(s) >= M:
        words.append(s)
words_times = collections.defaultdict(int)
for i in words:
    words_times[i] += 1
words = list(set(words))
words.sort(key=lambda x: (-words_times[x], -len(x), x))
for i in words:
    print(i)

