N = int(input())
for _ in range(N):
    H, W, N = map(int, input().split())
    floor = N % H
    line = (N // H) + 1
    if floor == 0:
        floor = H
        line -= 1
    if line <= 9:
        unit = f"{floor}0{line}"
    else:
        unit = f"{floor}{line}"
    print(unit)
