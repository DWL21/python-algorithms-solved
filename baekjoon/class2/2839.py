N = int(input())
max_five = N // 5
end = False
for i in range(max_five, -1, -1):
    n = (N - i * 5)
    if n % 3 == 0:
        print(n // 3 + i)
        end = True
        break
if not end:
    print(-1)
