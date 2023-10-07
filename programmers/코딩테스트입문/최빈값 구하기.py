def solution(array):
    numbers = [0] * 1001
    for i in array:
        numbers[i] += 1
    maximum = max(numbers)
    if numbers.count(maximum) > 1:
        return -1
    return numbers.index(maximum)
