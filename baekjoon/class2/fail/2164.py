import collections


N = int(input())
cards = collections.deque([i + 1 for i in range(N)])
index = -1
while len(cards) > 2:
    cards.popleft()
    cards.append(cards.popleft())
print(cards.pop())
