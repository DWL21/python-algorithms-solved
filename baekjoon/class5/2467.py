N = int(input())
numbers = list(map(int, input().split()))

answer = int(1e10) + 1
answer_right = 0
answer_left = 0

for i in range(0, N - 1):
    now = numbers[i]
    left = i + 1
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        total = now + numbers[mid]
        if abs(total) < answer:
            answer = abs(total)
            answer_left = i
            answer_right = mid
            if not total:
                break
        if total < 0:
            left = mid + 1
        else:
            right = mid - 1
        

print(numbers[answer_left], numbers[answer_right])
