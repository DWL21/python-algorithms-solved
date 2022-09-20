import sys

input = sys.stdin.readline

a_dic = dict()
answer = list()
N, M = map(int, input().split())
for _ in range(N):
    a_dic[input().rstrip()] = True
for _ in range(M):
    word = input().rstrip()
    if word in a_dic:
        answer.append(word)
answer.sort()
print(len(answer))
for i in answer:
    print(i)
