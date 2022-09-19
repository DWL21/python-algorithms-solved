import sys

input = sys.stdin.readline

dictionary = dict()
words = []
N, M = map(int, input().split())
count = 1
for _ in range(N):
    word = input().strip()
    dictionary[word] = count
    words.append(word)
    count += 1
for _ in range(M):
    case = input().strip()
    if case.isalpha():
        print(dictionary[case])
    else:
        print(words[int(case) - 1])
