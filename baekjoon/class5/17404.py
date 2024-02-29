import copy


N = int(input())
houses = []
for _ in range(N):
    houses.append(list(map(int, input().split())))

answer = int(1e9)

first_houses = copy.deepcopy(houses)
first_houses[1][0] = int(1e9)
first_houses[1][1] += first_houses[0][0]
first_houses[1][2] += first_houses[0][0]

for i in range(2, N):
    first_houses[i][0] += min(first_houses[i - 1][1], first_houses[i - 1][2])
    first_houses[i][1] += min(first_houses[i - 1][0], first_houses[i - 1][2])
    first_houses[i][2] += min(first_houses[i - 1][0], first_houses[i - 1][1])

answer = min(answer, first_houses[N - 1][1], first_houses[N - 1][2])

second_houses = copy.deepcopy(houses)
second_houses[1][0] += second_houses[0][1]
second_houses[1][1] = int(1e9)
second_houses[1][2] += second_houses[0][1]

for i in range(2, N):
    second_houses[i][0] += min(second_houses[i - 1][1], second_houses[i - 1][2])
    second_houses[i][1] += min(second_houses[i - 1][0], second_houses[i - 1][2])
    second_houses[i][2] += min(second_houses[i - 1][0], second_houses[i - 1][1])

answer = min(answer, second_houses[N - 1][0], second_houses[N - 1][2])

third_houses = copy.deepcopy(houses)
third_houses[1][0] += third_houses[0][2]
third_houses[1][1] += third_houses[0][2]
third_houses[1][2] += int(1e9)

for i in range(2, N):
    third_houses[i][0] += min(third_houses[i - 1][1], third_houses[i - 1][2])
    third_houses[i][1] += min(third_houses[i - 1][0], third_houses[i - 1][2])
    third_houses[i][2] += min(third_houses[i - 1][0], third_houses[i - 1][1])

answer = min(answer, third_houses[N - 1][0], third_houses[N - 1][1])

print(answer)
