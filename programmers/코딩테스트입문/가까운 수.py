def solution(array, n):
    numbers = []
    different = 1e9
    for i in array:
        x = max(i - n, n - i)
        if x < different:
            numbers = [i]
            different = x
        elif x == different:
            numbers.append(i)
    return min(numbers)
