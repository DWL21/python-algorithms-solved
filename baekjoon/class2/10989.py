N = int(input())
numbers = list()
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()
for i in numbers:
    print(i)
