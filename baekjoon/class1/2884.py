H, M = map(int, input().split())
answer = (H * 60 + M - 45) % (60 * 24)
print(f"{answer // 60} {answer % 60}")
