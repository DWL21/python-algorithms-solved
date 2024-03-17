from collections import defaultdict

N = int(input())
numbers = list(map(int, input().split()))
point = 0
histories = defaultdict(int)
histories[3] = numbers[0]
for i in range(1, N):
    new_histories = defaultdict(int)

    when5 = min(numbers[i], histories[3])
    new_histories[5] += when5
    histories[3] -= when5
    numbers[i] -= when5

    when7 = min(numbers[i], histories[5])
    histories[5] -= when7
    numbers[i] -= when7

    when3 = numbers[i]
    new_histories[3] += when3
    
    point += when7*7 + histories[5]*5 + histories[3]*3
    histories = new_histories

point += histories[3]*3 + histories[5]*5
print(point)