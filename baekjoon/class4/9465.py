T = int(input())
for _ in range(T):
    n = int(input())
    numbers = []
    for _ in range(2):
        numbers.append(list(map(int, input().split())))
    if n == 1:
        print(max(numbers[0][0], numbers[1][0]))
        continue
    if n == 2:
        print(max(numbers[0][0] + numbers[1][1], numbers[1][0] + numbers[0][1]))
        continue
    numbers[0][1] += numbers[1][0]
    numbers[1][1] += numbers[0][0]
    for i in range(2, n):
        numbers[0][i] += max(numbers[1][i - 1], numbers[0][i - 2], numbers[1][i - 2])
        numbers[1][i] += max(numbers[0][i - 1], numbers[0][i - 2], numbers[1][i - 2])
    answer = max(numbers[0][n - 1], numbers[1][n - 1])
    print(answer)
