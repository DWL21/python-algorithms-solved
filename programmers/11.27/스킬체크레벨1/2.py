def solution(N, stages):
    points = []
    for i in range(1, N + 1):
        a = 0
        b = 0
        for j in stages:
            if j == i:
                a += 1
                b += 1
            elif j > i:
                b += 1
        if b == 0:
            points.append((i, 0))
        else:
            points.append((i, a/b))
    points.sort(key=lambda x: (-x[1], x[0]))
    return list(map(lambda x: x[0], points))
