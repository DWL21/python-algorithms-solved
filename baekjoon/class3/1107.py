def solve(N, M):
    if M == 0:
        return len(str(N))
    buttons = list(map(str, input().split()))
    diff = 0
    while True:
        up = str(N + diff)
        down = str(N - diff)
        if not [x for i in up for x in buttons if i in x] or not [x for i in down for x in buttons if i in x]:
            break
        diff += 1
    answer = min(abs(N - 100), diff + min(len(str(N + diff)), len(str(N - diff))))
    return answer


print(solve(int(input()), int(input())))
