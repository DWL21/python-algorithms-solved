N, S = map(int, input().split())
numbers = list(map(int, input().split()))
left = 0
right = 0

buffer = numbers[0]

minimum = N + 1
while left < N and right < N:
    if left > right:
        right += 1
        buffer += numbers[right]
        continue
    if buffer >= S:
        minimum = min(minimum, right - left + 1)
        buffer -= numbers[left]
        left += 1
        continue
    right += 1
    if right < N:
        buffer += numbers[right]

if minimum > N:
    print(0)
else:
    print(minimum)
