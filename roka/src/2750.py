import sys

input = sys.stdin.readline

RANGE_RESTRICTION = 2002
    
N = int(input())
numbers = [False] * RANGE_RESTRICTION
for _ in range(N):
    numbers[int(input())] = True
for virtual_number, is_printing in enumerate(numbers[RANGE_RESTRICTION//2:]):
        if is_printing:
            print(virtual_number-RANGE_RESTRICTION//2)
for number, is_printing in enumerate(numbers[:RANGE_RESTRICTION//2]):
        if is_printing:
            print(number)
