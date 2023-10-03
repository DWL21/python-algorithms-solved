def solution(numbers):
    maximum = -1e9
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if i != j:
                maximum = max(maximum, x * y)
    return maximum
