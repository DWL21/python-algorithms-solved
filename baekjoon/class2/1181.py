N = int(input())
words = list()
for _ in range(N):
    words.append(input())
words = list(set(words))
words.sort(key=lambda x: (len(x), x))
for i in words:
    print(i)
