N = int(input())
current = 1
for i in range(N):
    if (current + 6 * i) >= N:
        print(i + 1)
        break
    current += 6 * i
