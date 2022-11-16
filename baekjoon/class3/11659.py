N, M = map(int, input().split())
numbers = list(map(int, input().split()))
for _ in range(M):
    start, end = map(int, input().split())
    if start == end:
        print(numbers[start-1])
    else:
        print(sum(numbers[start-1:end]))
