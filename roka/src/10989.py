import sys

input = sys.stdin.readline

N = int(input())
numbers = [0]*10001
for _ in range(N):
    numbers[int(input())] += 1
for number, counting in enumerate(numbers):
    for _ in range(counting):
        print(number)
