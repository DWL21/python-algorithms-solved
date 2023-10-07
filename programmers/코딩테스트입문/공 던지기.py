def solution(numbers, k):
    index = 2 * (k - 1)
    return numbers[index % len(numbers)]
