def solution(num, total):
    a = (2 * total // num + 1 - num) // 2
    return list(range(a, a + num))
