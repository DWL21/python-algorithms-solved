N = int(input())
points = list(map(int, input().split()))

answer = sum(points) / max(points) * 100 / N
print(answer)
