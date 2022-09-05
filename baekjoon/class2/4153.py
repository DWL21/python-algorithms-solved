while True:
    lines = list(map(int, input().split()))
    if sum(lines) == 0:
        break
    [a, b, c] = sorted(lines)
    if a * a + b * b == c * c:
        print("right")
    else:
        print("wrong")
