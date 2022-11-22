import bisect


def excluded(buttons, number):
    for i in str(number):
        if i in buttons:
            return True
    return False


def solve(N, M):
    diff_100 = abs(N - 100)
    if M == 0:
        return min(diff_100, len(str(N)))
    if M == 10:
        return diff_100
    buttons = list(map(str, input().split()))
    numbers = [i for i in range(1000000) if not excluded(buttons, i)]
    index = bisect.bisect_left(numbers, N)
    if index == 0:
        return min(diff_100, len(str(numbers[index])) + abs(numbers[index] - N))
    if index == len(numbers):
        return min(diff_100, len(str(numbers[-1])) + abs(numbers[-1] - N))
    return min(diff_100, abs(numbers[index - 1] - N) + len(str(numbers[index - 1])),
               abs(numbers[index] - N) + len(str(numbers[index])))


print(solve(int(input()), int(input())))
