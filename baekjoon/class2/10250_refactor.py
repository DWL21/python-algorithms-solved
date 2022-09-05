N = int(input())
for _ in range(N):
    H, W, N = map(int, input().split())
    print(str((N - 1) % H + 1) + str((N - 1) // H + 1).rjust(2, "0"))
