import bisect


def excluded(buttons, number):
    for i in str(number):
        if i in buttons:
            return True
    return False


def solve(N, M):
    number_length = len(str(N))
    diff_100 = abs(N - 100)
    if M == 0:
        return number_length
    if M == 10:
        return abs(100 - N)
    buttons = list(map(str, input().split()))
    numbers = [i for i in range(1000000) if not excluded(buttons, i)]
    index = bisect.bisect_left(numbers, N)
    if index == 0 or index == len(numbers):
        return min(diff_100, number_length + abs(numbers[-1] - N))
    if abs(numbers[index - 1] - N) < numbers[index] - N:
        return min(diff_100, abs(numbers[index - 1] - N) + len(str(numbers[index - 1])))
    else:
        return min(diff_100, numbers[index] - N + len(str(numbers[index])))


print(solve(int(input()), int(input())))
