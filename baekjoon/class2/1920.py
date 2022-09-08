import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
M = int(input())
checking_numbers = list(map(int, input().split()))
for i in checking_numbers:
    contains = False
    start_index = 0
    end_index = len(numbers) - 1
    while start_index <= end_index:
        mid = (start_index + end_index) // 2
        if numbers[mid] == i:
            print(1)
            contains = True
            break
        elif numbers[mid] > i:
            end_index = mid - 1
        else:
            start_index = mid + 1
    if not contains:
        print(0)
