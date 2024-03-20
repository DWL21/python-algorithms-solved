from collections import defaultdict

N, B, C = map(int, input().split())
numbers = list(map(int, input().split()))
point = 0
histories = defaultdict(int)

if B >= C:
    X = B 
    Y = B + C
    Z = B + 2*C

    histories[X] = numbers[0]
    for i in range(1, N):
        new_histories = defaultdict(int)

        when5 = min(numbers[i], histories[X])
        new_histories[Y] += when5
        histories[X] -= when5
        numbers[i] -= when5

        when7 = min(numbers[i], histories[Y])
        histories[Y] -= when7
        numbers[i] -= when7

        when3 = numbers[i]
        new_histories[X] += when3
        
        point += when7*Z + histories[Y]*Y + histories[X]*X
        histories = new_histories

    point += histories[X]*X + histories[Y]*Y
    print(point)
else:
    print(sum(numbers)*B)