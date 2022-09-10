import sys
import collections


input = sys.stdin.readline
numbers_count = collections.defaultdict(int)


N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
for i in numbers:
    numbers_count[i] += 1
answer = list()
for i in targets:
    answer.append(numbers_count[i])
print(" ".join(map(str, answer)))
