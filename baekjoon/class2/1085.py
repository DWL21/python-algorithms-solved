x, y, w, h = map(int, input().split())
minimum = min(abs(x-w), abs(y-h), x, y)
print(minimum)