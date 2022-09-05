T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    now_floor = list()
    next_floor = [i for i in range(1, n + 1)]

    for _ in range(k):
        now_floor = next_floor
        next_floor = list()
        for index, value in enumerate(now_floor):
            next_floor.append(sum(now_floor[:index + 1]))
    print(next_floor[n - 1])
