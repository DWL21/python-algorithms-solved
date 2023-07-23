import sys
from collections import defaultdict

input = sys.stdin.readline

ENTER = "ENTER"

times = 0
N = int(input())
chat_histories = defaultdict(bool)

for _ in range(N):
    s = input().rstrip()
    if s == ENTER:
        chat_histories.clear()
        continue
    if not chat_histories[s]:
        times += 1
        chat_histories[s] = True
print(times)

