N = int(input())
numbers = list(map(int, input().split()))
if N == 1:
    print(numbers[0]**2)
else:
    print(max(numbers) * min(numbers))

