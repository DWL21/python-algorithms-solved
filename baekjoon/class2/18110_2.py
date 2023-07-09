import sys


input = sys.stdin.readline


def round_new(n):
    if n >= int(n) + 0.5:
        return int(n) + 1
    return int(n)


people = [0] * 31
n = int(input())
if n == 0:
    print(0)
    exit(0)
for _ in range(n):
    people[int(input())] += 1
cutting = round_new(n * 0.15)

left_counting = cutting
left = 1
while left_counting > 0:
    if people[left] <= left_counting:
        left_counting -= people[left]
        people[left] = 0
    elif people[left] > left_counting:
        people[left] -= left_counting
        left_counting = 0
    left += 1

right_counting = cutting
right = 30
while right_counting > 0:
    if people[right] <= right_counting:
        right_counting -= people[right]
        people[right] = 0
    elif people[right] > right_counting:
        people[right] -= right_counting
        right_counting = 0
    right -= 1

total = 0
for i, value in enumerate(people):
    total += i * value
print(round_new(total / (n - 2*cutting)))

