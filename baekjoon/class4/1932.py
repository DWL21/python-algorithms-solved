n = int(input())
numbers = []
for _ in range(n):
    numbers.append(list(map(int, input().split())))


def solution(n, numbers):
    for i in reversed(range(n - 1)):
        now = numbers[i]
        for j, value in enumerate(now):
            now[j] += max(numbers[i + 1][j:j + 2])
    return numbers[0][0]


print(solution(n, numbers))

